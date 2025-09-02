"""Console interface for the 7-day planner."""
from __future__ import annotations

from .planner import Planner, pretty_print


def main() -> None:
    print("Planner7Days — quick 7-day learning roadmap generator")
    topic = input("Enter a topic (e.g. 'Python', 'ML', 'Git') [Python]: ") or "Python"
    p = Planner(topic=topic)
    plan = p.make_plan()
    pretty_print(plan)


if __name__ == "__main__":
    main()
