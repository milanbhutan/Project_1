import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import my_stats_lib as stats

# =================San Luis Obispo Weather=================
df_temp_prcp_SLO = pd.read_csv("SAN LUIS OBISPO POLY WEATHER.csv")
df_temp_prcp_fixed_SLO = (
    df_temp_prcp_SLO[["DATE", "TMAX", "PRCP"]]
    .dropna()
    .set_index("DATE")
    .sort_index()
    )

annual_max_temp_SLO = df_temp_prcp_fixed_SLO.loc[:, "TMAX"].to_numpy()
annual_prcp_SLO = df_temp_prcp_fixed_SLO.loc[:, "PRCP"].to_numpy()

avg_max_temp_SLO = stats.avg(annual_max_temp_SLO)
avg_prcp_SLO = stats.avg(annual_prcp_SLO)

var_max_temp_SLO = stats.var(annual_max_temp_SLO)
var_prcp_SLO = stats.var(annual_prcp_SLO)
temp_prcp_covar_SLO = stats.covar(annual_max_temp_SLO, annual_prcp_SLO)

m_SLO_temp, b_SLO_temp = np.polyfit(df_temp_prcp_fixed_SLO.index, df_temp_prcp_fixed_SLO["TMAX"], 1)
m_SLO_prcp, b_SLO_prcp = np.polyfit(df_temp_prcp_fixed_SLO.index, df_temp_prcp_fixed_SLO["PRCP"], 1)
r_SLO_temp = np.corrcoef(df_temp_prcp_fixed_SLO.index, df_temp_prcp_fixed_SLO["TMAX"])[0, 1]
r_SLO_prcp = np.corrcoef(df_temp_prcp_fixed_SLO.index, df_temp_prcp_fixed_SLO["PRCP"])[0, 1]

fig, axes = plt.subplots(2, 2)
fig.suptitle("Precipitation and Max Temperature \n for past 100 years in SLO")

temp_bins_SLO = np.arange(68, 80, 1)
prcp_bins_SLO = np.arange(5, 55, 5)

axes[0, 0].plot(df_temp_prcp_fixed_SLO[["TMAX"]], marker = ".")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Max Temperature ($^\circ$F)")

axes[0, 1].hist(df_temp_prcp_fixed_SLO["TMAX"], bins = temp_bins_SLO, edgecolor = "black")
axes[0, 1].set_xticks(temp_bins_SLO)
axes[0, 1].set_xlabel("Max Temperature ($^\circ$F)")
axes[0, 1].set_ylabel("Count")

axes[1, 0].plot(df_temp_prcp_fixed_SLO[["PRCP"]], marker = ".")
axes[1, 0].set_xlabel("Year")
axes[1, 0].set_ylabel("Precipitation (Inches)")

axes[1, 1].hist(df_temp_prcp_fixed_SLO["PRCP"], bins = prcp_bins_SLO, edgecolor = "black")
axes[1, 1].set_xlabel("Precipitation (Inches)")
axes[1, 1].set_ylabel("Count")

print("\n===============SLO===============")
print(f"Max Temperature Average: {avg_max_temp_SLO}")
print(f"Precipitation Average: {avg_prcp_SLO}")
print(f"Max Temperature Variance: {var_max_temp_SLO}")
print(f"Precipitation Variance: {var_prcp_SLO}")
print(f"Temperature and Precipitation Covariance: \n{temp_prcp_covar_SLO}")
print(f"Max Temperature Trendline Slope: {m_SLO_temp}")
print(f"Max Temperature Trendline Offset: {b_SLO_temp}")
print(f"Max Temperature Correlation Coefficient: {r_SLO_temp}")
print(f"Precipitation Trendline Slope: {m_SLO_prcp}")
print(f"Precipitation Trendline Offset: {b_SLO_prcp}")
print(f"Precipitation Correlation Coefficient: {r_SLO_prcp}")

# =================Fairbanks, AK Weather=================
df_temp_prcp_FAIR = pd.read_csv("FAIRBANKS WEATHER.csv")
df_temp_prcp_fixed_FAIR = (
    df_temp_prcp_FAIR[["DATE", "TMAX", "PRCP"]]
    .dropna()
    .set_index("DATE")
    .sort_index()
    )

annual_max_temp_FAIR = df_temp_prcp_fixed_FAIR.loc[:, "TMAX"].to_numpy()
annual_prcp_FAIR = df_temp_prcp_fixed_FAIR.loc[:, "PRCP"].to_numpy()

avg_max_temp_FAIR = stats.avg(annual_max_temp_FAIR)
avg_prcp_FAIR = stats.avg(annual_prcp_FAIR)

var_max_temp_FAIR = stats.var(annual_max_temp_FAIR)
var_prcp_FAIR = stats.var(annual_prcp_FAIR)
temp_prcp_covar_FAIR = stats.covar(annual_max_temp_FAIR, annual_prcp_FAIR)

m_FAIR_temp, b_FAIR_temp = np.polyfit(df_temp_prcp_fixed_FAIR.index, df_temp_prcp_fixed_FAIR["TMAX"], 1)
m_FAIR_prcp, b_FAIR_prcp = np.polyfit(df_temp_prcp_fixed_FAIR.index, df_temp_prcp_fixed_FAIR["PRCP"], 1)
r_FAIR_temp = np.corrcoef(df_temp_prcp_fixed_FAIR.index, df_temp_prcp_fixed_FAIR["TMAX"])[0, 1]
r_FAIR_prcp = np.corrcoef(df_temp_prcp_fixed_FAIR.index, df_temp_prcp_fixed_FAIR["PRCP"])[0, 1]

fig_2, axes_2 = plt.subplots(2, 2)
fig_2.suptitle("Precipitation and Max Temperature \n for past 100 years in Fairbanks, AK")

temp_bins_FAIR = np.arange(30, 45, 1)
prcp_bins_FAIR = np.arange(5, 20, 1)

axes_2[0, 0].plot(df_temp_prcp_fixed_FAIR[["TMAX"]], marker = ".")
axes_2[0, 0].set_xlabel("Year")
axes_2[0, 0].set_ylabel("Max Temperature ($^\circ$F)")

axes_2[0, 1].hist(df_temp_prcp_fixed_FAIR["TMAX"], bins = temp_bins_FAIR, edgecolor = "black")
axes_2[0, 1].set_xticks(temp_bins_FAIR)
axes_2[0, 1].set_xlabel("Max Temperature ($^\circ$F)")
axes_2[0, 1].set_ylabel("Count")

axes_2[1, 0].plot(df_temp_prcp_fixed_FAIR[["PRCP"]], marker = ".")
axes_2[1, 0].set_xlabel("Year")
axes_2[1, 0].set_ylabel("Precipitation (Inches)")

axes_2[1, 1].hist(df_temp_prcp_fixed_FAIR["PRCP"], bins = prcp_bins_FAIR, edgecolor = "black")
axes_2[1, 1].set_xlabel("Precipitation (Inches)")
axes_2[1, 1].set_ylabel("Count")

print("\n===============Fairbanks, AK===============")
print(f"Max Temperature Average: {avg_max_temp_FAIR}")
print(f"Precipitation Average: {avg_prcp_FAIR}")
print(f"Max Temperature Variance: {var_max_temp_FAIR}")
print(f"Precipitation Variance: {var_prcp_FAIR}")
print(f"Temperature and Precipitation Covariance: \n{temp_prcp_covar_FAIR}")
print(f"Max Temperature Trendline Slope: {m_FAIR_temp}")
print(f"Max Temperature Trendline Offset: {b_FAIR_temp}")
print(f"Max Temperature Correlation Coefficient: {r_FAIR_temp}")
print(f"Precipitation Trendline Slope: {m_FAIR_prcp}")
print(f"Precipitation Trendline Offset: {b_FAIR_prcp}")
print(f"Precipitation Correlation Coefficient: {r_FAIR_prcp}")


# =================SLO and Fairbanks; Precipitation vs. Temperature=================
fig_3 = plt.figure()
plt.scatter(df_temp_prcp_fixed_FAIR["PRCP"], df_temp_prcp_fixed_FAIR["TMAX"], label = "Fairbanks, AK")
plt.scatter(df_temp_prcp_fixed_SLO["PRCP"], df_temp_prcp_fixed_SLO["TMAX"], label = "SLO")
plt.xlabel("Precipitation (Inches)")
plt.ylabel("Temperature ($^\circ$F)")
plt.title("Precipitation vs. Temperature")
plt.legend()
plt.grid()
plt.show()