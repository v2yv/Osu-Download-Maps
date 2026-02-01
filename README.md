# osu! Map Downloader Bot

A Telegram bot that downloads osu! beatmaps directly from osu.ppy.sh using a specific SOCKS5 proxy and session authentication. This allows downloading maps that are otherwise restricted or require login.

## Features

- **SOCKS5 Proxy Support**: Routes traffic through a configured proxy.
- **Session Authentication**: Uses `osu_session` cookie to access downloads.
- **Telegram Integration**: Send a link, get the `.osz` file.
- **Docker Support**: Easy deployment with Docker Compose.
- **PEP 8 Compliance**: Clean and readable Python code.

## Prerequisites

- Python 3.10+ (for local run)
- Docker & Docker Compose (for containerized run)
- Telegram Bot Token (from @BotFather)
- Valid `osu_session` cookie

## Configuration

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
OSU_SESSION=your_osu_session_cookie_value
PROXY_URL=socks5://user:pass@host:port
```

_Note: The `PROXY_URL` and `OSU_SESSION` are likely already pre-configured for this specific project instance._

## Installation & Usage

### Method 1: Docker (Recommended)

1.  Build and run the container:
    ```bash
    docker-compose up -d --build
    ```
2.  The bot is now running in the background.

### Method 2: Local Python

1.  Create a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    # source venv/bin/activate  # Linux/Mac
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the bot:
    ```bash
    python bot.py
    ```

## Testing

You can verify the download logic without the bot interface using the test script:

```bash
python test_download.py
```
