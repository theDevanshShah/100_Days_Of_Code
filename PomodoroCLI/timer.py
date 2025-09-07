"""Simple, testable Pomodoro timer core."""
from __future__ import annotations
from dataclasses import dataclass


class PomodoroTimer:
    """A simple, non-blocking pomodoro state machine.

    It supports giving durations either as minutes (default) or direct seconds
    via the ``*_seconds`` parameters (useful for tests).
    """

    def __init__(self, *, work_minutes: float = 25.0, short_break: float = 5.0, long_break: float = 15.0,
                 cycles_before_long: int = 4, work_seconds: int | None = None,
                 short_break_seconds: int | None = None, long_break_seconds: int | None = None):
        if work_seconds is not None:
            self.work = float(work_seconds)
        else:
            self.work = float(work_minutes) * 60.0
        if short_break_seconds is not None:
            self.short_break = float(short_break_seconds)
        else:
            self.short_break = float(short_break) * 60.0
        if long_break_seconds is not None:
            self.long_break = float(long_break_seconds)
        else:
            self.long_break = float(long_break) * 60.0

        self.cycles_before_long = int(cycles_before_long)
        self.reset()

    def reset(self) -> None:
        """Reset the timer to the initial work phase."""
        self.current_phase: str = "work"
        self.remaining: float = float(self.work)
        self.cycle_count: int = 0
        self.running: bool = False

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def tick(self, seconds: float) -> None:
        """Advance the timer by `seconds` (non-blocking).

        If the remaining time reaches zero the phase advances automatically.
        """
        if not self.running:
            return
        if seconds <= 0:
            return
        self.remaining = max(0.0, self.remaining - float(seconds))
        if self.remaining == 0.0:
            self._advance_phase()

    def _advance_phase(self) -> None:
        if self.current_phase == "work":
            self.cycle_count += 1
            if self.cycles_before_long > 0 and self.cycle_count % self.cycles_before_long == 0:
                self.current_phase = "long_break"
                self.remaining = float(self.long_break)
            else:
                self.current_phase = "short_break"
                self.remaining = float(self.short_break)
        else:
            self.current_phase = "work"
            self.remaining = float(self.work)

    def is_running(self) -> bool:
        return bool(self.running)

    def __repr__(self) -> str:
        return f"<PomodoroTimer phase={self.current_phase!r} remaining={self.remaining!r} cycles={self.cycle_count} running={self.running}>"
