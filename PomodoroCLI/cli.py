"""Small CLI wrapper around PomodoroTimer for demonstration."""
from __future__ import annotations
import argparse
import time
from .timer import PomodoroTimer


def main():
    parser = argparse.ArgumentParser(prog="pomodoro-cli", description="Tiny Pomodoro CLI (non-blocking demo)")
    parser.add_argument("--work", type=float, default=25.0, help="work minutes (default 25)")
    parser.add_argument("--short", type=float, default=5.0, help="short break minutes (default 5)")
    parser.add_argument("--long", type=float, default=15.0, help="long break minutes (default 15)")
    parser.add_argument("--cycles", type=int, default=4, help="cycles before long break (default 4)")
    args = parser.parse_args()

    timer = PomodoroTimer(work_minutes=args.work, short_break=args.short, long_break=args.long, cycles_before_long=args.cycles)
    print("Starting Pomodoro (press Ctrl+C to stop). This demo advances every second.")
    try:
        timer.start()
        while True:
            print(f"Phase: {timer.current_phase:12} Remaining: {int(timer.remaining)}s Cycles: {timer.cycle_count}", end="\r")
            time.sleep(1)
            timer.tick(1)
    except KeyboardInterrupt:
        print("\nStopped")


if __name__ == "__main__":
    main()
