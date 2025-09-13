# PomodoroCLI

A tiny, testable Pomodoro timer library and CLI demo created as a small project for the 100 Days of Code workspace.

Files:
- `PomodoroCLI/timer.py` — core, non-blocking state machine (easy to unit test).
- `PomodoroCLI/cli.py` — small CLI demo that advances the timer every second.
- `PomodoroCLI/tests/test_timer.py` — unit tests.

Quick run (demo):

```bash
python -m PomodoroCLI.cli --work 0.05 --short 0.01 --long 0.02 --cycles 2
```

(This uses fractional minutes for a quick demo.)
