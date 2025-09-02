import builtins
import unittest
from unittest import mock

from MiniMathTutor import app


class TestMiniMathTutor(unittest.TestCase):
    def test_generate_question_variety(self):
        q = app.generate_question(difficulty=1)
        self.assertTrue(hasattr(q, "text"))
        self.assertTrue(hasattr(q, "answer"))

    def test_division_precision(self):
        with mock.patch.object(app.random, "choice", lambda _ : "/"):
            q = app.generate_question(difficulty=1)
            self.assertIsInstance(q.answer, float)

    def test_run_quiz_no_time_limit(self):
        # provide three quick answers (strings). They don't need to be correct.
        answers = ["1", "2", "3"]
        with mock.patch.object(builtins, "input", side_effect=answers):
            stats = app.run_quiz(rounds=3, difficulty=1, time_limit=None)
            self.assertEqual(stats["asked"], 3)


if __name__ == "__main__":
    unittest.main()
