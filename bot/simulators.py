import pyautogui
from .interfaces import IInputSimulator


class PyAutoGuiInputSimulator(IInputSimulator):

  def click(self, x: int, y: int) -> None:
    pyautogui.click(x, y)