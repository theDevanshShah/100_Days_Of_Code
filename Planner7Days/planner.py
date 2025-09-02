"""Simple 7-day planner generator for beginners.

Generates a roadmap of bite-sized daily tasks for learning a topic (e.g., Python, ML).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class DayPlan:
    day: int
    title: str
    tasks: List[str]


class Planner:
    """Create a 7-day roadmap for a chosen topic.

    Example usage:
        p = Planner(topic="Python basics")
        plan = p.make_plan()
    """

    def __init__(self, topic: str = "Python basics") -> None:
        self.topic = topic

    def make_plan(self) -> List[DayPlan]:
        t = self.topic.lower()
        if "python" in t:
            return self._python_plan()
        if "ml" in t or "machine" in t:
            return self._ml_plan()
        if "git" in t:
            return self._git_plan()
        # fallback: general study plan
        return self._general_plan()

    def _python_plan(self) -> List[DayPlan]:
        return [
            DayPlan(1, "Setup & Syntax", ["Install Python & set up venv", "Run simple scripts: print(), variables"]),
            DayPlan(2, "Control Flow", ["if/else", "for and while loops", "practice small problems"]),
            DayPlan(3, "Data Structures", ["lists, tuples, dicts, sets", "indexing and slicing"]),
            DayPlan(4, "Functions & Modules", ["write functions", "import modules, use pip"]),
            DayPlan(5, "File I/O & Errors", ["read/write files", "try/except"]),
            DayPlan(6, "Testing & Debugging", ["write simple tests", "use print/debugger"]),
            DayPlan(7, "Mini Project", ["build a small CLI app (todo/planner)", "publish or share code"]),
        ]

    def _ml_plan(self) -> List[DayPlan]:
        return [
            DayPlan(1, "Math basics", ["linear algebra review", "basic probability"]),
            DayPlan(2, "Python for ML", ["numpy basics", "pandas quick intro"]),
            DayPlan(3, "Supervised Learning", ["linear regression", "classification overview"]),
            DayPlan(4, "Models & Evaluation", ["train/test split", "metrics: accuracy, loss"]),
            DayPlan(5, "Neural Networks intro", ["perceptron -> activation functions", "simple feedforward"]),
            DayPlan(6, "Hands-on", ["train a tiny model on toy data", "visualize results"]),
            DayPlan(7, "Mini Project", ["build a small classifier and write a report"]),
        ]

    def _git_plan(self) -> List[DayPlan]:
        return [
            DayPlan(1, "Git basics", ["install git", "git init, status, add, commit"]),
            DayPlan(2, "Branching", ["create branches", "merge and resolve conflicts"]),
            DayPlan(3, "Remote", ["push/pull", "use GitHub basics"]),
            DayPlan(4, "Workflows", ["fork & PR flow", "review basics"]),
            DayPlan(5, "Advanced", ["rebase, stash", "tags and release"]),
            DayPlan(6, "Automation", ["CI basics", "simple GitHub Actions"]),
            DayPlan(7, "Project", ["publish a small repo", "write README & license"]),
        ]

    def _general_plan(self) -> List[DayPlan]:
        return [
            DayPlan(1, "Goal & Setup", ["define goal", "gather tools"]),
            DayPlan(2, "Foundations", ["learn core concepts", "watch 1-2 tutorials"]),
            DayPlan(3, "Practice", ["small exercises", "take notes"]),
            DayPlan(4, "Deepen", ["read docs or a chapter", "try an example"]),
            DayPlan(5, "Review", ["revise notes", "fix gaps"]),
            DayPlan(6, "Apply", ["small project", "ask for feedback"]),
            DayPlan(7, "Reflect & Next steps", ["document learning", "plan next week"]),
        ]


def pretty_print(plan: List[DayPlan]) -> None:
    for d in plan:
        print(f"Day {d.day}: {d.title}")
        for t in d.tasks:
            print(f"  - {t}")
        print()


if __name__ == "__main__":
    p = Planner(topic="Python basics")
    pretty_print(p.make_plan())
