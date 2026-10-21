import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    mtrx_a = np.array(a)
    mtrx_b = np.array(b)
    if np.linalg.norm(a)==0 * np.linalg.norm(b)==0:
        return float(0)
    return float((mtrx_a @ mtrx_b) / (np.linalg.norm(a)* np.linalg.norm(b)))