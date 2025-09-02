import unittest

from Planner7Days.planner import Planner


class TestPlanner(unittest.TestCase):
    def test_python_plan_length(self):
        p = Planner(topic="Python")
        plan = p.make_plan()
        self.assertEqual(len(plan), 7)

    def test_ml_plan_contains_neural(self):
        p = Planner(topic="Machine Learning")
        plan = p.make_plan()
        titles = [d.title.lower() for d in plan]
        self.assertTrue(any("neural" in t or "net" in t for t in titles))


if __name__ == "__main__":
    unittest.main()
