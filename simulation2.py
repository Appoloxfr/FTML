import numpy as np


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
