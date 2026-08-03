import pandas as pd
from sqlalchemy import create_engine


db_path = "Database/bluestock_mf.db"


engine = create_engine(
    f"sqlite:///{db_path}"
)


file_path = "Data/01_fund_master.csv"


df = pd.read_csv(file_path)


print("Fund Master Rows:", len(df))


df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)


print("Fund master loaded successfully")

# Load NAV history

nav_file = "Data/02_nav_history.csv"


nav_df = pd.read_csv(nav_file)


print("NAV History Rows:", len(nav_df))


nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)


print("NAV history loaded successfully")

# Load AUM data

aum_file = "Data/03_aum_by_fund_house.csv"


aum_df = pd.read_csv(aum_file)


print("AUM Rows:", len(aum_df))


aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)


print("AUM data loaded successfully")

# Load SIP inflows data

sip_file = "Data/04_monthly_sip_inflows.csv"


sip_df = pd.read_csv(sip_file)


print("SIP Inflow Rows:", len(sip_df))


sip_df.to_sql(
    "fact_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)


print("SIP inflows loaded successfully")

# Load category inflows data

category_file = "Data/05_category_inflows.csv"


category_df = pd.read_csv(category_file)


print("Category Inflow Rows:", len(category_df))


category_df.to_sql(
    "fact_category_inflows",
    engine,
    if_exists="replace",
    index=False
)


print("Category inflows loaded successfully")

# Load industry folio count data

folio_file = "Data/06_industry_folio_count.csv"


folio_df = pd.read_csv(folio_file)


print("Folio Count Rows:", len(folio_df))


folio_df.to_sql(
    "fact_folio_count",
    engine,
    if_exists="replace",
    index=False
)


print("Folio count loaded successfully")

# Load scheme performance data

performance_file = "Data/07_scheme_performance.csv"


performance_df = pd.read_csv(performance_file)


print("Performance Rows:", len(performance_df))


performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)


print("Performance data loaded successfully")

# Load investor transactions data

transaction_file = "Data/08_investor_transactions.xlsx"


transaction_df = pd.read_excel(transaction_file)


print("Transaction Rows:", len(transaction_df))


transaction_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)


print("Transactions loaded successfully")

# Load portfolio holdings data

portfolio_file = "Data/09_portfolio_holdings.csv"


portfolio_df = pd.read_csv(portfolio_file)


print("Portfolio Rows:", len(portfolio_df))


portfolio_df.to_sql(
    "fact_portfolio",
    engine,
    if_exists="replace",
    index=False
)


print("Portfolio holdings loaded successfully")

# Load benchmark indices data

benchmark_file = "Data/10_benchmark_indices.csv"


benchmark_df = pd.read_csv(benchmark_file)


print("Benchmark Rows:", len(benchmark_df))


benchmark_df.to_sql(
    "fact_benchmark",
    engine,
    if_exists="replace",
    index=False
)


print("Benchmark indices loaded successfully")