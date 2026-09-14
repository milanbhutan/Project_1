import numpy as np

def avg(
    x: np.ndarray
):
    return (np.sum(x) / np.size(x) )

def var(
    x: np.ndarray
) -> float:
    mu_x = avg(x)
    variance = np.sum((x - mu_x) ** 2) / np.size(x)
    return variance

def covar(
    x: np.ndarray,
    y: np.ndarray,
) -> np.ndarray:
    mu_x = avg(x)
    mu_y = avg(y)
    z = np.vstack((x, y))
    mean_vec = np.array([[mu_x], [mu_y]])
    covariance = ((z - mean_vec) @ (z - mean_vec).T) / np.size(x)

    return covariance