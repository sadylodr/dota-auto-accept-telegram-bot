import numpy as np
from abc import ABC, abstractmethod, abstractmethod


class IScreenCapturer(ABC):

  @abstractmethod
  def capture(self) -> np.ndarray:
    pass


class IMatchDetector(ABC):

  @abstractmethod
  def detect(
      self, frame: np.ndarray
  ) -> tuple[bool, tuple[int, int] | None]:
    pass


class IInputSimulator(ABC):

  @abstractmethod
  def click(self, x: int, y: int) -> None:
    pass


class INotifier(ABC):

  @abstractmethod
  def send(self, message: str) -> None:
    pass