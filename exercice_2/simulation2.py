import numpy as np
from typing import Callable

rand = np.random.default_rng()


def absolute_loss(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Compute the absolute loss between two arrays.

    Args:
        x (np.ndarray): The first array.
        y (np.ndarray): The second array.

    Returns:
        np.ndarray: The absolute loss between x and y.
    """
    return np.abs(x - y)


def square_loss(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Compute the square loss between two arrays.

    Args:
        x (np.ndarray): The first array.
        y (np.ndarray): The second array.

    Returns:
        np.ndarray: The square loss between x and y.
    """
    return (x - y) ** 2


def create_data(n: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Create synthetic data for regression.

    Args:
        n (int): The number of data points to generate.

    Returns:
        tuple: A tuple containing the generated X and Y arrays.
    """
    X = np.random.uniform(0.1, 0.5, n)
    Y = np.random.geometric(X)

    return X, Y


def wrong_estimator(X: np.array) -> np.array:
    """
    A bad estimator that returns random values between 0.1 and 0.9
    for each input.

    Args:
        X (np.array): Input array.

    Returns:
        np.array: Array of random values between 0.1 and 0.9.
    """
    return np.random.uniform(0.1, 0.9, size=len(X))


def square_bayes(X: np.array) -> np.array:
    """
    Square Bayes predictor that calculates the reciprocal of each input value in the array.

    Args:
        X (np.array): Input array.

    Returns:
        np.array: Array of square Bayes predictor values.
    """
    return 1 / X


def absolute_bayes(X: np.array) -> np.array:
    """
    Absolute Bayes predictor that calculates the ceiling of (-log(2)
    / log(1 - X)) for each input.

    Args:
        X (np.array): Input array.

    Returns:
        np.array: Array of absolute Bayes predictor values.
    """
    return np.ceil((-np.log(2)) / np.log(1 - X))


def compute_risk(
    estimator: Callable[[np.ndarray], np.ndarray],
    loss: Callable[[np.ndarray, np.ndarray], np.ndarray],
    X: np.ndarray,
    Y: np.ndarray,
) -> float:
    """
    Calculate the empirical risk given an estimator, a loss function, and input-output data.

    Args:
        estimator (Callable[[np.ndarray], np.ndarray]): A function
            that takes X and returns Y.
        loss (Callable[[np.ndarray, np.ndarray], np.ndarray]):
            A function that takes two values and returns a loss.
        X (np.ndarray): Input array.
        Y (np.ndarray): Output array.

    Returns:
        float: The empirical risk.
    """
    predictions = estimator(X)
    losses = loss(Y, predictions)
    return losses.mean()


X, Y = create_data(int(1e6))
print(f"X = {X}")
print(f"Y = {Y}")
print()

print("With the square loss:")
print(f"Bad estimator: {compute_risk(wrong_estimator, square_loss, X, Y)}")
print(f"Absolute Bayes predictor: {compute_risk(absolute_bayes, square_loss, X, Y)}")
print(f"Squared Bayes predictor: {compute_risk(square_bayes, square_loss, X, Y)}")
print()

print("With the absolute loss:")
print(f"Bad estimator: {compute_risk(wrong_estimator, absolute_loss, X, Y)}")
print(f"Absolute Bayes predictor: {compute_risk(absolute_bayes, absolute_loss, X, Y)}")
print(f"Squared Bayes predictor: {compute_risk(square_bayes, absolute_loss, X, Y)}")
