import asyncio
import os
from dotenv import load_dotenv
from downloader import OsuDownloader

# Ensure env vars are loaded
load_dotenv()


async def test():
    # Example URL from user request
    url = "https://osu.ppy.sh/beatmapsets/2486143#fruits/5457747"
    print(f"Testing download for: {url}")

    downloader = OsuDownloader()
    try:
        file_path = await downloader.download_beatmapset(url)
        print(f"Successfully downloaded to: {file_path}")

        # verify file size > 0
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            print("File is valid.")
        else:
            print("File is empty or missing.")

    except Exception as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    asyncio.run(test())
