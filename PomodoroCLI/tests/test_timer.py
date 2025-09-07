import pytest
from PomodoroCLI.timer import PomodoroTimer


def test_cycle_transitions():
    # use explicit seconds so tests are deterministic and fast
    t = PomodoroTimer(work_seconds=3, short_break_seconds=1, long_break_seconds=2, cycles_before_long=2)
    assert t.current_phase == "work"
    assert int(t.remaining) == 3
    t.start()

    # finish first work period -> short break
    t.tick(3)
    assert t.current_phase == "short_break"
    assert t.cycle_count == 1

    # finish short break -> back to work
    t.tick(1)
    assert t.current_phase == "work"

    # finish second work period -> long break (cycles_before_long=2)
    t.tick(3)
    assert t.current_phase == "long_break"
    assert t.cycle_count == 2


def test_tick_while_stopped_noop():
    t = PomodoroTimer(work_seconds=2)
    t.reset()
    t.tick(2)
    # since timer not started, phase should not advance
    assert t.current_phase == "work"


def test_reset():
    t = PomodoroTimer(work_seconds=2, short_break_seconds=1)
    t.start()
    t.tick(2)
    assert t.current_phase == "short_break"
    t.reset()
    assert t.current_phase == "work"
    assert int(t.remaining) == 2
