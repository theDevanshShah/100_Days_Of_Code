import unittest

from ToyPerceptron.perceptron import Perceptron


class TestPerceptron(unittest.TestCase):
    def test_predict_initial(self):
        p = Perceptron(n_inputs=2)
        preds = p.predict([[0, 0], [1, 1]])
        # initial weights 0 -> bias 0 -> activation of 0 yields 1 (since >=0): 1
        self.assertEqual(preds, [1, 1])

    def test_train_and_gate(self):
        X = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y_and = [0, 0, 0, 1]
        p = Perceptron(n_inputs=2)
        p.train(X, y_and, epochs=20, lr=0.1)
        preds = p.predict(X)
        # perceptron should learn the AND gate
        self.assertEqual(preds, y_and)


if __name__ == "__main__":
    unittest.main()
