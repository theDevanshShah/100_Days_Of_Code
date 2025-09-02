"""Simple perceptron implementation for binary classification.

Designed for beginners to see how weights, bias and training steps work.
"""
from __future__ import annotations

from typing import List, Tuple


class Perceptron:
    """A tiny perceptron that learns a linear decision boundary.

    Usage:
        p = Perceptron(n_inputs=2)
        p.train(X, y, epochs=10, lr=0.1)
        preds = p.predict(X)
    """

    def __init__(self, n_inputs: int = 2) -> None:
        self.n_inputs = n_inputs
        # initialize small weights and bias
        self.weights = [0.0 for _ in range(n_inputs)]
        self.bias = 0.0

    def activation(self, x: float) -> int:
        return 1 if x >= 0 else 0

    def predict_one(self, inputs: List[float]) -> int:
        s = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return self.activation(s)

    def predict(self, X: List[List[float]]) -> List[int]:
        return [self.predict_one(x) for x in X]

    def train(self, X: List[List[float]], y: List[int], epochs: int = 10, lr: float = 0.1) -> None:
        for _ in range(epochs):
            for xi, yi in zip(X, y):
                pred = self.predict_one(xi)
                error = yi - pred
                # update
                for j in range(self.n_inputs):
                    self.weights[j] += lr * error * xi[j]
                self.bias += lr * error


def demo_and_train():
    # Simple AND gate dataset
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y_and = [0, 0, 0, 1]
    p = Perceptron(n_inputs=2)
    p.train(X, y_and, epochs=10, lr=0.1)
    return p


if __name__ == "__main__":
    p = demo_and_train()
    print("Weights:", p.weights)
    print("Bias:", p.bias)
    print("Predictions on AND:", p.predict([[0,0],[0,1],[1,0],[1,1]]))
