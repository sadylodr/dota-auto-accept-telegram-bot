import os
from dotenv import load_dotenv
from bot import (
    DotaMatchBot,
    OpenCVMatchDetector,
    PyAutoGuiInputSimulator,
    PyAutoGuiScreenCapturer,
    TelegramNotifier,
)


def main():
  load_dotenv()

  TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
  CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
  CHECK_INTERVAL = float(os.getenv("CHECK_INTERVAL", 1.0))
  POST_CLICK_DELAY = float(os.getenv("POST_CLICK_DELAY", 30.0))
  CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.82))

  TEMPLATE_FILE = "assets/accept_button.png"

  if not TELEGRAM_TOKEN or not CHAT_ID:
    print(
        "[ERROR] Need to set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in the .env file."
    )
    return

  screen_capturer = PyAutoGuiScreenCapturer()
  match_detector = OpenCVMatchDetector(
      TEMPLATE_FILE, confidence=CONFIDENCE_THRESHOLD
  )
  input_simulator = PyAutoGuiInputSimulator()
  telegram_notifier = TelegramNotifier(token=TELEGRAM_TOKEN, chat_id=CHAT_ID)

  bot = DotaMatchBot(
      capturer=screen_capturer,
      detector=match_detector,
      simulator=input_simulator,
      notifier=telegram_notifier,
      check_interval=CHECK_INTERVAL,
      post_click_delay=POST_CLICK_DELAY,
  )

  bot.run()


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("\nScript stopped by user.")