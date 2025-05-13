# timer/timer_manager.py
import time

class TimerManager:
    def __init__(self):
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = time.time()
        self._end_time = None

    def stop(self):
        if self._start_time is not None:
            self._end_time = time.time()

    def reset(self):
        self._start_time = None
        self._end_time = None

    def get_duration(self):
        if self._start_time is None:
            return 0
        if self._end_time is None:
            return time.time() - self._start_time
        return self._end_time - self._start_time

    def get_duration_str(self):
        duration = self.get_duration()
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        return f"{minutes:02d}:{seconds:02d}"
