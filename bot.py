import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from config import BOT_TOKEN
from downloader import OsuDownloader

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
downloader = OsuDownloader()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Send me an osu! beatmap link, and I will download it for you."
    )


@dp.message(F.text.regexp(r"https://osu\.ppy\.sh/beatmapsets/\d+"))
async def handle_osu_link(message: types.Message):
    url = message.text.strip()
    status_msg = await message.answer(
        "Downloading beatmap... This may take a moment."
    )

    try:
        file_path = await downloader.download_beatmapset(url)

        await status_msg.edit_text("Uploading to Telegram...")

        beatmap_file = FSInputFile(file_path)
        await message.answer_document(beatmap_file)

        await status_msg.delete()

        # Cleanup
        os.remove(file_path)

    except Exception as e:
        await status_msg.edit_text(f"Error: {e}")
        logging.error(f"Download failed: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
