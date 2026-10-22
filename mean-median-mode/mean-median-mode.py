from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean = np.mean(x)
    median = np.median(x)
    mode = Counter(x)
    return {"mean": float(mean), "median": float(median), "mode": float(mode.most_common(1)[0][0])}