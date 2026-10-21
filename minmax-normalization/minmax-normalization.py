import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    X_arr = np.array(X)
    _min = np.min(X_arr, axis=axis, keepdims=True)
    _max = np.max(X_arr, axis=axis, keepdims=True)
    # max_matrix = np.full(X_arr.shape, max)
    # min_matrix = np.full(X_arr.shape, _min)
    return (X_arr-_min) / ((_max-_min) + eps)