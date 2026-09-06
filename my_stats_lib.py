import numpy as np

def avg(
    x: np.ndarray
):
    return (np.sum(x) / np.size(x) )


def covar(
    x: np.ndarray,
    y: np.ndarray,
) -> np.ndarray:
    u_x = avg(x)
    u_y = avg(y)
    z = np.vstack((x, y))
    mean_vec = np.array([[u_x], [u_y]])
    covariance = ((z - mean_vec) @ (z - mean_vec).T) / (np.size(x) - 1)

    return covariance