import numpy as np


def create_y(X: np.ndarray) -> np.ndarray:
    """
    Generate an ndarray of y values based on the given ndarray of
    X values.

    Args:
        X (np.ndarray): ndarray of values.

    Returns:
        np.ndarray: ndarray of corresponding y values.

    """
    y = np.where(
        X < 1, np.random.uniform(0, 1, size=X.shape), np.random.normal(X, size=X.shape)
    )
    return y


def predict_bayes(X: np.ndarray) -> np.ndarray:
    """
    Generate an ndarray of predicted y values based on the given
    ndarray of X values using a Bayesian prediction approach.

    Args:
        X (np.ndarray): ndarray of values.

    Returns:
        np.ndarray: ndarray of predicted y values.

    """
    y = np.where(X < 1, 1 / 2, X)
    return y


def predict_tilde(X: np.ndarray) -> np.ndarray:
    """
    Return the input ndarray of values as is.

    Args:
        X (np.ndarray): ndarray of values.

    Returns:
        np.ndarray: Input ndarray of values.

    """
    return X


def statistical_approximation(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute the statistical approximation between two ndarrays of
    true and predicted values.

    Args:
        y_true (np.ndarray): ndarray of true values.
        y_pred (np.ndarray): ndarray of predicted values.

    Returns:
        float: Mean squared difference between y_true and y_pred.

    """
    return np.mean((y_true - y_pred) ** 2)  # type: ignore


X = np.random.randint(3, size=1000000)
y = create_y(X)

f_bayes = predict_bayes(X)
f_tilde = predict_tilde(X)

stat_val_tilde = statistical_approximation(y, predict_tilde(X))
real_bayes_risk = 1 / 24 + 2 / 3

print("With statistical approximation of the tilde risk which is:", stat_val_tilde)
print("With the bayes risk which is:", real_bayes_risk)
