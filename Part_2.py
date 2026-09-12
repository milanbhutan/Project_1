import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import my_stats_lib as stats

df_temp_prcp = pd.read_csv("SAN LUIS OBISPO POLY WEATHER.csv")
df_temp_prcp_fixed = (
    df_temp_prcp[["DATE", "TMAX", "PRCP"]]
    .dropna()
    .set_index("DATE")
    .sort_index()
    )
annual_max_temp = df_temp_prcp_fixed.loc[:, "TMAX"].to_numpy()
annual_prcp = df_temp_prcp_fixed.loc[:, "PRCP"].to_numpy()

avg_max_temp = stats.avg(annual_max_temp)
avg_prcp = stats.avg(annual_prcp)

var_max_temp = stats.var(annual_max_temp)
var_prcp = stats.var(annual_prcp)
temp_prcp_covar = stats.covar(annual_max_temp, annual_prcp)


fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(df_temp_prcp_fixed[["TMAX"]])

print(f"Max Temperature Average: {avg_max_temp}")
print(f"Precipitation Average: {avg_prcp}")
print(f"Max Temperature Variance: {var_max_temp}")
print(f"Precipitation Variance: {var_prcp}")
print(f"Temperature and Precipitation Covariance: \n{temp_prcp_covar}")

plt.show()