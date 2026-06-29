import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tickers = ["AAPL", "MSFT", "NVDA", "TSM", "TSLA", "GOOG",]

data = yf.download(tickers, start = "2020-01-01", end = "2026-01-01")

price = data["Close"]

#Santiy Check (commented out after verification)
#print(price.head())

returns = price.pct_change().dropna()
correlation = returns.corr()


#Santiy Check (Commented out after verification)
#print(correlation.round(2))


flat = correlation.unstack()
mask = ~np.eye(len(correlation), dtype = bool)
clean = correlation.where(mask)
print(mask)

pairs = correlation.where(mask).unstack().dropna()


pairs = pairs.sort_values(ascending=False)
print(pairs)

pairs = pairs.drop_duplicates().head(5)
print("Most correlated pairs:")
print(pairs)

plt.figure(figsize=(10,8))

fig, axes = plt.subplots (1,2, figsize = (18,8))


sns.heatmap(correlation,
            mask = np.eye(len(correlation), dtype = bool),
            annot=True, 
            cmap="coolwarm", 
            vmin= -1, 
            vmax= 1, 
            fmt = ".2f", 
            ax = axes[0])

axes[0].set_title("Correlation of Daily Returns")

top5 = (correlation.where(~np.eye(len(correlation), dtype = bool))
.unstack().dropna()
.sort_values(ascending=False)
.drop_duplicates()
.head(5))

labels = [f"{a}-{b}" for a, b in top5.index]

axes[1].bar(labels, top5.values, color = "steelblue")

axes[1].set_title("Top 5 Most Correlated Assets")
axes[1].set_ylabel("Correlation")


plt.tight_layout()
plt.savefig("Correlation_Heatmap.png", dpi = 1500, bbox_inches = "tight")
plt.show()

