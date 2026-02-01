import os
import re
import httpx
from fake_useragent import UserAgent
from config import PROXY_URL, OSU_SESSION


class OsuDownloader:
    def __init__(self):
        self.proxy_url = PROXY_URL
        self.session_cookie = OSU_SESSION
        self.base_url = "https://osu.ppy.sh"
        self.ua = UserAgent()

    async def download_beatmapset(self, url: str):
        beatmapset_id_match = re.search(r"beatmapsets/(\d+)", url)
        if not beatmapset_id_match:
            raise ValueError("Invalid osu! beatmap URL")

        beatmapset_id = beatmapset_id_match.group(1)
        download_url = f"{self.base_url}/beatmapsets/{beatmapset_id}/download"

        headers = {
            "User-Agent": self.ua.random,
            "Cookie": f"osu_session={self.session_cookie}",
            "Referer": url,
            "Origin": self.base_url
        }

        async with httpx.AsyncClient(
            proxies=self.proxy_url,
            follow_redirects=True,
            timeout=60.0
        ) as client:
            async with client.stream("GET", download_url, headers=headers) as response:
                if response.status_code != 200:
                    raise Exception(
                        f"Failed to download. Status code: {response.status_code}"
                    )

                if "osu.ppy.sh/home" in str(response.url):
                    raise Exception(
                        "Session invalid or expired. Please update osu_session."
                    )

                content_disposition = response.headers.get("content-disposition")
                if content_disposition:
                    filename_match = re.findall(
                        'filename="?([^"]+)"?', content_disposition
                    )
                    if filename_match:
                        filename = filename_match[0]
                    else:
                        filename = f"{beatmapset_id}.osz"
                else:
                    filename = f"{beatmapset_id}.osz"

                filename = re.sub(r'[\\/*?:"<>|]', "", filename)

                os.makedirs("downloads", exist_ok=True)
                file_path = os.path.join("downloads", filename)

                with open(file_path, "wb") as f:
                    async for chunk in response.aiter_bytes():
                        f.write(chunk)

                return file_path
