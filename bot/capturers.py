import cv2
import numpy as np
import pyautogui
from .interfaces import IScreenCapturer


class PyAutoGuiScreenCapturer(IScreenCapturer):

  def capture(self) -> np.ndarray:
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)