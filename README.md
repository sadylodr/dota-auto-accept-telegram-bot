# DotaAutoAccept

Automatically accepts found Dota 2 matches and notifies you through Telegram.

The bot scans the screen for the accept-button template in `assets/accept_button.png`. When it finds a match, it clicks the button and sends a Telegram message.

## Quick start

**Windows**

```powershell
# Create and activate the environment
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Configure Telegram and bot settings
Copy-Item .env.example .env
# Edit .env with your values

# Run
.\run.bat
```

**macOS / Linux**

```bash
# Create and activate the environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure Telegram and bot settings
cp .env.example .env
# Edit .env with your values

# Run
python3 main.py
```

On Windows, you can also start the bot directly with `python main.py` after activating the virtual environment.

## Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | Required |
| `TELEGRAM_CHAT_ID` | Chat receiving notifications | Required |
| `CHECK_INTERVAL` | Seconds between screen scans | `1.0` |
| `POST_CLICK_DELAY` | Seconds to wait after accepting | `30.0` |
| `CONFIDENCE_THRESHOLD` | OpenCV template-match threshold | `0.82` |

Create a Telegram bot with [@BotFather](https://t.me/BotFather), start a chat with it, and set the resulting token and chat ID in `.env`.

## Stop

Press `Ctrl+C` in the running terminal.

> The bot controls your mouse and clicks the first matching screen location. Keep Dota 2 visible, verify the template image matches your UI scale, and use it only where automation is permitted.
