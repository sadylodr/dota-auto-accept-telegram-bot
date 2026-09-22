import time
from .interfaces import IInputSimulator, IMatchDetector, INotifier, IScreenCapturer


class DotaMatchBot:

  def __init__(
      self,
      capturer: IScreenCapturer,
      detector: IMatchDetector,
      simulator: IInputSimulator,
      notifier: INotifier,
      check_interval: float = 1.0,
      post_click_delay: float = 30.0,
  ):
    self._capturer = capturer
    self._detector = detector
    self._simulator = simulator
    self._notifier = notifier
    self._check_interval = check_interval
    self._post_click_delay = post_click_delay

  def run(self) -> None:
    print("=" * 60)
    print(" Screen scanning is active. To exit: Ctrl + C")
    print("=" * 60)

    while True:
      try:
        frame = self._capturer.capture()
        found, coords = self._detector.detect(frame)

        if found and coords:
          x, y = coords
          print(f"[SUCCESS] Match has been found! Clicking on coordinates: X={x}, Y={y}")

          self._simulator.click(x, y)
          self._notifier.send(
              "🎮 Match in Dota 2 found and accepted automatically! Come back"
              " to the PC."
          )

          print(f"Waiting for the draft stage ({self._post_click_delay} seconds)...")
          time.sleep(self._post_click_delay)
        else:
          time.sleep(self._check_interval)

      except KeyboardInterrupt:
        print("\nScript stopped by user.")
        break
      except Exception as e:
        print(f"[Error in loop] {e}")
        time.sleep(2)