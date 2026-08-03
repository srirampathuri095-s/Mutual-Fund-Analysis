-- =====================================================
-- Mutual Fund Analysis
-- Analytical SQL Queries
-- =====================================================


-- 1. Top 5 Funds by AUM
-- Shows funds with highest assets under management

SELECT 
    f.scheme_name,
    f.fund_house,
    a.aum_lakh_crore,
    a.year
FROM fact_aum a
JOIN dim_fund f
ON a.fund_id = f.fund_id
ORDER BY a.aum_lakh_crore DESC
LIMIT 5;



-- 2. Average NAV per Month

SELECT
    strftime('%Y-%m', d.full_date) AS month,
    AVG(n.nav) AS average_nav
FROM fact_nav n
JOIN dim_date d
ON n.date_id = d.date_id
GROUP BY month
ORDER BY month;



-- 3. SIP Year-over-Year Growth

SELECT
    year,
    SUM(sip_inflow_crore) AS total_sip_inflow,
    LAG(SUM(sip_inflow_crore)) OVER(
        ORDER BY year
    ) AS previous_year_inflow,

    (
        (SUM(sip_inflow_crore) -
        LAG(SUM(sip_inflow_crore)) OVER(
            ORDER BY year
        ))
        /
        LAG(SUM(sip_inflow_crore)) OVER(
            ORDER BY year
        )
    ) * 100 AS yoy_growth_percentage

FROM fact_sip_inflows
GROUP BY year;



-- 4. Transactions by State

SELECT
    state,
    COUNT(transaction_id) AS total_transactions,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;



-- 5. Funds with Expense Ratio Less Than 1%

SELECT
    f.scheme_name,
    f.fund_house,
    p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id = f.fund_id
WHERE p.expense_ratio_pct < 1
ORDER BY p.expense_ratio_pct;



-- 6. Top Performing Funds by 5 Year Return

SELECT
    f.scheme_name,
    f.fund_house,
    p.return_5yr_pct
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id = f.fund_id
ORDER BY p.return_5yr_pct DESC
LIMIT 10;



-- 7. Average Return by Fund Category

SELECT
    f.category,
    AVG(p.return_3yr_pct) AS avg_3yr_return
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id = f.fund_id
GROUP BY f.category
ORDER BY avg_3yr_return DESC;



-- 8. Highest SIP Investment Age Groups

SELECT
    age_group,
    COUNT(transaction_id) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY age_group
ORDER BY total_amount DESC;



-- 9. Portfolio Sector Allocation

SELECT
    sector,
    SUM(weight_pct) AS total_weight
FROM fact_portfolio
GROUP BY sector
ORDER BY total_weight DESC;



-- 10. Fund Risk and Performance Analysis

SELECT
    f.scheme_name,
    f.risk_grade,
    p.return_3yr_pct,
    p.sharpe_ratio,
    p.std_dev_ann_pct
FROM fact_performance p
JOIN dim_fund f
ON p.fund_id = f.fund_id
ORDER BY p.sharpe_ratio DESC;