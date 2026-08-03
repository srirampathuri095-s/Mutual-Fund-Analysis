CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE NOT NULL,
    scheme_name TEXT NOT NULL,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_date DATE UNIQUE NOT NULL,
    day INTEGER,
    month INTEGER,
    month_name TEXT,
    quarter INTEGER,
    year INTEGER
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT NOT NULL,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    transaction_type TEXT,
    amount_inr REAL NOT NULL,
    state TEXT,
    city TEXT,
    payment_mode TEXT,
    kyc_status TEXT,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    aum_lakh_crore REAL NOT NULL,

    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

