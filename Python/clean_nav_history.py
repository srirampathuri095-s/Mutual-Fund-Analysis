import pandas as pd

nav = pd.read_csv("Data/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(by=["amfi_code", "date"])

nav = nav.drop_duplicates()

print("Number of rows after removing duplicates:", len(nav))

print(nav["nav"].isnull().sum())

invalid_nav = nav[nav["nav"] <= 0]

print("Invalid NAV values:", len(invalid_nav))

nav.to_csv("Data/processed/02_nav_history.csv", index=False)

print("Cleaned NAV history saved successfully!")