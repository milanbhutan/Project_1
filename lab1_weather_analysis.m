%% Import Date, PRCP, TAVG, TMAX, and TMIN columns from CSV file using Import Tool
%eliminate any NaN entries
Dates_PRCP = DATE(~isnan(PRCP));
PRCP = PRCP(~isnan(PRCP));

Dates_TAVG = DATE(~isnan(TAVG));
TAVG = TAVG(~isnan(TAVG));

Dates_TMAX = DATE(~isnan(TMAX));
TMAX = TMAX(~isnan(TMAX));

Dates_TMIN = DATE(~isnan(TMIN));
TMIN = TMIN(~isnan(TMIN));

%% Plotting Data and Histograms
figure(1)
plot(Dates_PRCP, PRCP,"LineStyle","-","LineWidth",3,"Color","r","Marker","o","MarkerSize",5);
title("Precipitation vs Time","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Year","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Precipitation [inches]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
grid on;
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(2)
histogram(PRCP,"FaceColor","r")
title("Precipitation Histogram","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Precipitation [inches]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Count","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(3)
plot(Dates_TAVG, TAVG,"LineStyle","-","LineWidth",3,"Color","g","Marker","o","MarkerSize",5);
title("Avg. Temperature vs Time","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Year","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Avg. Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
grid on;
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(4)
histogram(TAVG,"FaceColor","g")
title("Avg. Temperature Histogram","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Avg. Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Count","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(5)
plot(Dates_TMAX, TMAX,"LineStyle","-","LineWidth",3,"Color","cyan","Marker","o","MarkerSize",5);
title("Max Temperature vs Time","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Year","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Max Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
grid on;
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(6)
histogram(TMAX,"FaceColor","b")
title("Max Temperature Histogram","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Max Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Count","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(7)
plot(Dates_TMIN, TMIN,"LineStyle","-","LineWidth",3,"Color","m","Marker","o","MarkerSize",5);
title("Min Temperature vs Time","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Year","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Min Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
grid on;
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(8)
histogram(TMIN,"FaceColor","m")
title("Min Temperature Histogram","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Min Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Count","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

%% Averages & Variances
mean_PRCP = sum(PRCP)/length(PRCP);
var_PRCP = sum((PRCP - mean_PRCP).^2)/(length(PRCP) - 1);

mean_TAVG = sum(TAVG)/length(TAVG);
var_TAVG = sum((TAVG - mean_TAVG).^2)/(length(TAVG) - 1);

mean_TMAX = sum(TMAX)/length(TMAX);
var_TMAX = sum((TMAX - mean_TMAX).^2)/(length(TMAX) - 1);

mean_TMIN = sum(TMIN)/length(TMIN);
var_TMIN = sum((TMIN - mean_TMIN).^2)/(length(TMIN) - 1);

%% Covariance Matrix Computations
Dates_PRCP_TAVG = intersect(Dates_PRCP,Dates_TAVG);
PRCP_ = PRCP(ismember(Dates_PRCP,Dates_PRCP_TAVG));
TAVG_ = TAVG(ismember(Dates_TAVG,Dates_PRCP_TAVG));
X_PRCP_TAVG = [PRCP_ TAVG_];
mu_PRCP_TAVG = (sum(X_PRCP_TAVG,1)/(size(X_PRCP_TAVG,1)))';
Z_PRCP_TAVG = zeros(2);
for i = 1:size(X_PRCP_TAVG,1)
    Xi = X_PRCP_TAVG(i,:)';
    Z_PRCP_TAVG = Z_PRCP_TAVG + ((Xi-mu_PRCP_TAVG)*(Xi-mu_PRCP_TAVG)');
end
Z_PRCP_TAVG = Z_PRCP_TAVG/(size(X_PRCP_TAVG,1)-1);

Dates_PRCP_TMAX = intersect(Dates_PRCP,Dates_TMAX);
PRCP_ = PRCP(ismember(Dates_PRCP,Dates_PRCP_TMAX));
TMAX_ = TMAX(ismember(Dates_TMAX,Dates_PRCP_TMAX));
X_PRCP_TMAX = [PRCP_ TMAX_];
mu_PRCP_TMAX = (sum(X_PRCP_TMAX,1)/(size(X_PRCP_TMAX,1)))';
Z_PRCP_TMAX = zeros(2);
for i = 1:size(X_PRCP_TMAX,1)
    Xi = X_PRCP_TMAX(i,:)';
    Z_PRCP_TMAX = Z_PRCP_TMAX + ((Xi-mu_PRCP_TMAX)*(Xi-mu_PRCP_TMAX)');
end
Z_PRCP_TMAX = Z_PRCP_TMAX/(size(X_PRCP_TMAX,1)-1);

Dates_PRCP_TMIN = intersect(Dates_PRCP,Dates_TMIN);
PRCP_ = PRCP(ismember(Dates_PRCP,Dates_PRCP_TMIN));
TMIN_ = TMIN(ismember(Dates_TMIN,Dates_PRCP_TMIN));
X_PRCP_TMIN = [PRCP_ TMIN_];
mu_PRCP_TMIN = (sum(X_PRCP_TMIN,1)/(size(X_PRCP_TMIN,1)))';
Z_PRCP_TMIN = zeros(2);
for i = 1:size(X_PRCP_TMIN,1)
    Xi = X_PRCP_TMIN(i,:)';
    Z_PRCP_TMIN = Z_PRCP_TMIN + ((Xi-mu_PRCP_TMIN)*(Xi-mu_PRCP_TMIN)');
end
Z_PRCP_TMIN = Z_PRCP_TMIN/(size(X_PRCP_TMIN,1)-1);

%% Scatter Plots
load("SLO_DATA.mat");
SLO_X_PRCP_TAVG = X_PRCP_TAVG;
SLO_X_PRCP_TMAX = X_PRCP_TMAX;
SLO_X_PRCP_TMIN = X_PRCP_TMIN;

load("FAIRBANKS_DATA.mat");
FB_X_PRCP_TAVG = X_PRCP_TAVG;
FB_X_PRCP_TMAX = X_PRCP_TMAX;
FB_X_PRCP_TMIN = X_PRCP_TMIN;

figure(9)
scatter(SLO_X_PRCP_TAVG(:,1),SLO_X_PRCP_TAVG(:,2), 25, "r", "o", "filled")
hold on
scatter(FB_X_PRCP_TAVG(:,1),FB_X_PRCP_TAVG(:,2), 25, "cyan", "o", "filled")
title("San Luis Obispo vs Fairbanks Weather","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Precipitation [inches]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Avg. Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
legend("San Luis Obispo, CA","Fairbanks, AK")
grid on
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(10)
scatter(SLO_X_PRCP_TMAX(:,1),SLO_X_PRCP_TMAX(:,2), 25, "r", "o", "filled")
hold on
scatter(FB_X_PRCP_TMAX(:,1),FB_X_PRCP_TMAX(:,2), 25, "cyan", "o", "filled")
title("San Luis Obispo vs Fairbanks Weather","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Precipitation [inches]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Max Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
legend("San Luis Obispo, CA","Fairbanks, AK")
grid on
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;

figure(11)
scatter(SLO_X_PRCP_TMIN(:,1),SLO_X_PRCP_TMIN(:,2), 25, "r", "o", "filled")
hold on
scatter(FB_X_PRCP_TMIN(:,1),FB_X_PRCP_TMIN(:,2), 25, "cyan", "o", "filled")
title("San Luis Obispo vs Fairbanks Weather","FontName","TimesNewRoman","FontSize",15,"FontWeight","bold");
xlabel("Precipitation [inches]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
ylabel("Min Temperature [{\circ}F]","FontName","TimesNewRoman","FontSize",14,"FontWeight","bold");
legend("San Luis Obispo, CA","Fairbanks, AK")
grid on
ax = gca; ax.FontSize = 14; ax.FontWeight = "bold"; ax.LineWidth = 1.5;