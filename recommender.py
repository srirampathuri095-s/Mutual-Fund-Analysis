
import sqlite3
import pandas as pd


DB_PATH = "Database/bluestock_mf.db"


def recommend_funds(risk_appetite):

    risk_appetite = risk_appetite.strip().title()

    valid_risks = ["Low", "Moderate", "High"]

    if risk_appetite not in valid_risks:
        print("Invalid risk appetite.")
        print("Choose: Low, Moderate, or High")
        return None

    conn = sqlite3.connect(DB_PATH)

    funds = pd.read_sql("""
        SELECT
            amfi_code,
            scheme_name,
            category,
            risk_grade,
            sharpe_ratio
        FROM fact_performance
    """, conn)

    conn.close()

    recommendations = (
        funds[
            funds["risk_grade"] == risk_appetite
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
        .reset_index(drop=True)
    )

    recommendations.index = recommendations.index + 1

    return recommendations[
        [
            "amfi_code",
            "scheme_name",
            "category",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]


if __name__ == "__main__":

    risk = input(
        "Enter risk appetite (Low/Moderate/High): "
    )

    result = recommend_funds(risk)

    if result is not None:
        print("\nTop 3 Recommended Funds:")
        print(result.to_string(index=True))
