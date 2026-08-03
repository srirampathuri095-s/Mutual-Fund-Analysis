from sqlalchemy import create_engine, text


engine = create_engine(
    "sqlite:///Database/bluestock_mf.db"
)


tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_sip_inflows",
    "fact_category_inflows",
    "fact_folio_count",
    "fact_performance",
    "fact_transactions",
    "fact_portfolio",
    "fact_benchmark"
]


with engine.connect() as conn:

    for table in tables:

        result = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )

        count = result.scalar()

        print(table, ":", count, "rows")