# Mutual Fund Analysis - Data Dictionary


## Table 1: dim_fund

Source File:
01_fund_master.csv


Column Details:

fund_id
- Data Type: INTEGER
- Meaning: Unique ID for each fund

amfi_code
- Data Type: INTEGER
- Meaning: AMFI scheme code

scheme_name
- Data Type: TEXT
- Meaning: Name of mutual fund scheme

fund_house
- Data Type: TEXT
- Meaning: Asset management company name

category
- Data Type: TEXT
- Meaning: Mutual fund category

plan
- Data Type: TEXT
- Meaning: Direct or Regular plan

risk_grade
- Data Type: TEXT
- Meaning: Risk level of fund

## Table 2: dim_date

Source File:
Generated from date fields


Column Details:

date_id
- Data Type: INTEGER
- Meaning: Unique ID for each date


full_date
- Data Type: DATE
- Meaning: Complete calendar date


day
- Data Type: INTEGER
- Meaning: Day number


month
- Data Type: INTEGER
- Meaning: Month number


month_name
- Data Type: TEXT
- Meaning: Name of month


quarter
- Data Type: INTEGER
- Meaning: Financial quarter


year
- Data Type: INTEGER
- Meaning: Calendar year

## Table 3: fact_nav

Source File:
02_nav_history.csv


Column Details:

nav_id
- Data Type: INTEGER
- Meaning: Unique ID for NAV record


fund_id
- Data Type: INTEGER
- Meaning: Reference ID of mutual fund


date_id
- Data Type: INTEGER
- Meaning: Reference ID of date


nav
- Data Type: REAL
- Meaning: Net Asset Value of the fund

## Table 4: fact_transactions

Source File:
08_investor_transactions.xlsx


Column Details:

transaction_id
- Data Type: INTEGER
- Meaning: Unique transaction ID


investor_id
- Data Type: TEXT
- Meaning: Unique investor identifier


fund_id
- Data Type: INTEGER
- Meaning: Reference ID of mutual fund


date_id
- Data Type: INTEGER
- Meaning: Reference ID of transaction date


transaction_type
- Data Type: TEXT
- Meaning: Type of transaction (SIP, Lumpsum, Redemption)


amount_inr
- Data Type: REAL
- Meaning: Transaction amount in Indian Rupees


state
- Data Type: TEXT
- Meaning: Investor state


city
- Data Type: TEXT
- Meaning: Investor city


payment_mode
- Data Type: TEXT
- Meaning: Mode of payment


kyc_status
- Data Type: TEXT
- Meaning: Investor KYC verification status

## Table 5: fact_performance

Source File:
07_scheme_performance.csv


Column Details:

performance_id
- Data Type: INTEGER
- Meaning: Unique performance record ID


fund_id
- Data Type: INTEGER
- Meaning: Reference ID of mutual fund


return_1yr_pct
- Data Type: REAL
- Meaning: One year fund return percentage


return_3yr_pct
- Data Type: REAL
- Meaning: Three year fund return percentage


return_5yr_pct
- Data Type: REAL
- Meaning: Five year fund return percentage


benchmark_3yr_pct
- Data Type: REAL
- Meaning: Benchmark return for three years


alpha
- Data Type: REAL
- Meaning: Extra return compared to benchmark


beta
- Data Type: REAL
- Meaning: Market risk measurement


sharpe_ratio
- Data Type: REAL
- Meaning: Risk adjusted return measurement


sortino_ratio
- Data Type: REAL
- Meaning: Downside risk adjusted return


std_dev_ann_pct
- Data Type: REAL
- Meaning: Annual volatility percentage


max_drawdown_pct
- Data Type: REAL
- Meaning: Maximum loss percentage


expense_ratio_pct
- Data Type: REAL
- Meaning: Annual fund management expense percentage


morningstar_rating
- Data Type: INTEGER
- Meaning: Fund rating score

## Table 6: fact_aum

Source File:
03_aum_by_fund_house.csv


Column Details:

aum_id
- Data Type: INTEGER
- Meaning: Unique AUM record ID


fund_id
- Data Type: INTEGER
- Meaning: Reference ID of mutual fund


year
- Data Type: INTEGER
- Meaning: Year of AUM measurement


aum_lakh_crore
- Data Type: REAL
- Meaning: Assets Under Management value in lakh crore

