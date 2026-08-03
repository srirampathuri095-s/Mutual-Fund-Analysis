import pandas as pd

performance = pd.read_csv("Data/07_scheme_performance.csv")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    performance[col] = pd.to_numeric(performance[col], errors="coerce")

print(performance[return_columns].isnull().sum())

anomalies = performance[
    (performance["return_1yr_pct"] < -100) |
    (performance["return_1yr_pct"] > 100) |
    (performance["return_3yr_pct"] < -100) |
    (performance["return_3yr_pct"] > 100) |
    (performance["return_5yr_pct"] < -100) |
    (performance["return_5yr_pct"] > 100)
]

print("Anomalous return records:", len(anomalies))

invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("Invalid expense ratio records:", len(invalid_expense))

performance.to_csv(
    "Data/processed/07_scheme_performance.csv",
    index=False
)

print("Cleaned scheme performance saved successfully!")