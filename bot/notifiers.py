import requests
from .interfaces import INotifier


class TelegramNotifier(INotifier):

  def __init__(self, token: str, chat_id: str):
    self.token = token
    self.chat_id = chat_id
    self.url = f"https://api.telegram.org/bot{token}/sendMessage"

  def send(self, message: str) -> None:
    try:
      payload = {"chat_id": self.chat_id, "text": message}
      response = requests.post(self.url, json=payload, timeout=5)
      response.raise_for_status()
    except Exception as e:
      print(f"[Telegram Error] Не удалось отправить уведомление: {e}")