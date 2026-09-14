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


fig, axes = plt.subplots(2, 2)
fig.suptitle("Precipitation and Max Temperature \n for past 100 years in SLO")

temp_bins = np.arange(68, 80, 1)
prcp_bins = np.arange(5, 55, 5)

axes[0, 0].plot(df_temp_prcp_fixed[["TMAX"]], marker = ".")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Max Temperature ($^\circ$F)")

axes[0, 1].hist(df_temp_prcp_fixed["TMAX"], bins = temp_bins, edgecolor = "black")
axes[0, 1].set_xticks(temp_bins)
axes[0, 1].set_xlabel("Max Temperature ($^\circ$F)")
axes[0, 1].set_ylabel("Count")

axes[1, 0].plot(df_temp_prcp_fixed[["PRCP"]], marker = ".")
axes[1, 0].set_xlabel("Year")
axes[1, 0].set_ylabel("Precipitation (Inches)")

axes[1, 1].hist(df_temp_prcp_fixed["PRCP"], bins = prcp_bins, edgecolor = "black")
#axes[1, 1].set_xticks(bins)
axes[1, 1].set_xlabel("Precipitation (Inches)")
axes[1, 1].set_ylabel("Count")

print(f"Max Temperature Average: {avg_max_temp}")
print(f"Precipitation Average: {avg_prcp}")
print(f"Max Temperature Variance: {var_max_temp}")
print(f"Precipitation Variance: {var_prcp}")
print(f"Temperature and Precipitation Covariance: \n{temp_prcp_covar}")





plt.show()