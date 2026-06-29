# Market Correlation Heatmap

A small project that downloads historical stock prices, computes the
correlation of their daily returns, and visualizes the result as a heatmap —
plus a bar chart of the most correlated pairs. Built as a hands-on
introduction to portfolio risk concepts and Python's data/plotting stack.

## What it does

1. Downloads daily price data (2020–2026) for: `AAPL`, `MSFT`, `NVDA`, `TSM`,
   `TSLA`, `GOOG`.
2. Converts prices into daily returns and computes the correlation matrix
   between every pair of stocks.
3. Plots the matrix as a heatmap, with same-stock cells masked out instead of
   showing a meaningless 1.00.
4. Plots a bar chart of the top 5 most correlated pairs alongside it.

Output: `Correlation_Heatmap.png`, a two-panel image (heatmap + bar chart).

## Why correlation, not price

Stock prices generally trend upward together over time, which makes raw
prices look falsely correlated. Daily **returns** strip out that trend and
reveal how stocks actually move *relative to each other* day to day — which
is what matters for portfolio risk.

## Key takeaway

Several of these tickers (e.g. `AAPL`/`MSFT`, or `NVDA`/`TSM` given the chip
supply-chain link) tend to be highly correlated, because they share common
drivers — sector trends, macro conditions, or supply-chain exposure. A
portfolio that looks diversified by number of holdings can still be risky if
those holdings move together — real diversification comes from combining
assets with **low or negative** correlation, not just *more* assets.

## Setup

Requires Python 3 and the following libraries:

```bash
pip3 install yfinance pandas numpy seaborn matplotlib
```

## Usage

```bash
python3 Heatmap.py
```

Outputs:
- Printed correlation pairs in the terminal (sorted, most correlated first).
- `Correlation_Heatmap.png` — the heatmap + top-5 bar chart.

## Tech stack

- [yfinance](https://pypi.org/project/yfinance/) — price data
- [pandas](https://pandas.pydata.org/) — returns & correlation calculations
- [numpy](https://numpy.org/) — diagonal masking
- [matplotlib](https://matplotlib.org/) / [seaborn](https://seaborn.pydata.org/) — plotting
