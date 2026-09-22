import cv2
import numpy as np
from .interfaces import IMatchDetector


class OpenCVMatchDetector(IMatchDetector):

  def __init__(self, template_path: str, confidence: float = 0.82):
    self.confidence = confidence
    self.template = cv2.imread(template_path)
    if self.template is None:
      raise FileNotFoundError(
          f"Шаблон кнопки не найден по пути: '{template_path}'"
      )
    self.h, self.w = self.template.shape[:2]

  def detect(self, frame: np.ndarray) -> tuple[bool, tuple[int, int] | None]:
    result = cv2.matchTemplate(frame, self.template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= self.confidence:
      center_x = max_loc[0] + self.w // 2
      center_y = max_loc[1] + self.h // 2
      return True, (center_x, center_y)

    return False, None