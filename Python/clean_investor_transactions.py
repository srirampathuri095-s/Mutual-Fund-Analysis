import pandas as pd

transactions = pd.read_excel("Data/08_investor_transactions.xlsx")

transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

transactions["transaction_type"] = transactions["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

invalid_amount = transactions[transactions["amount_inr"] <= 0]

print("Invalid transaction amounts:", len(invalid_amount))
print("Unique KYC Status values:")
print(transactions["kyc_status"].unique())
valid_kyc = ["Verified", "Pending"]

invalid_kyc = transactions[~transactions["kyc_status"].isin(valid_kyc)]

print("Invalid KYC records:", len(invalid_kyc))
transactions.to_csv(
    "Data/processed/08_investor_transactions.csv",
    index=False
)

print("Cleaned investor transactions saved successfully!")