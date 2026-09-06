import numpy as np
import matplotlib as plt
import my_stats_lib as my_stats

x = [1 ,2, 2, 4]
y = [3, 4, 5, 1]

py_avg = np.average(x)
my_avg = my_stats.avg(x)

py_covar = np.cov(x, y)
my_covar = my_stats.covar(x, y)

print(py_avg)
print(my_avg)

print(py_covar)
print(my_covar)
