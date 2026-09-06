import numpy as np
import matplotlib as plt
import pandas as pd
import my_stats_lib as my_stats

df_temp_prcp = pd.read_csv("Datasets/SLO_annual_temp_and_precip.csv")
annual_max_temp = df_temp_prcp.loc[:, "TMAX"]
annual_prcp = df_temp_prcp.loc[:, "PRCP"]


avg_max_temp = my_stats.avg(annual_max_temp)
avg_prcp = my_stats.avg(annual_prcp)
# my_covar = my_stats.covar(x, y)

print(avg_max_temp)
print(avg_prcp)

#print(my_covar)
