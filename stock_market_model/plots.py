from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv("sp500.csv")
df = pd.read_csv("sp500_paper.csv")


sp_log_returns = np.log(df["Close"]) - np.log(df["Open"])

normalized_sp_log_returns = (sp_log_returns - sp_log_returns.mean()) / sp_log_returns.std()

with Path("his2.npy").open('rb') as f:
    model_log_retruns = np.load(f)
model_log_retruns =np.sum(model_log_retruns,axis=1)
normalized_model_log_retruns = (model_log_retruns - model_log_retruns.mean()) / model_log_retruns.std()


print(np.max(normalized_model_log_retruns))
print(np.argmax(normalized_model_log_retruns))

print(np.min(normalized_model_log_retruns))
print(np.argmin(normalized_model_log_retruns))

plt.figure("121")
percs = np.linspace(0.1, 99.9, 100)
qn_a = np.percentile(normalized_model_log_retruns, percs)
qn_b = np.percentile(normalized_sp_log_returns, percs)

plt.plot(qn_a, qn_b, ls="", marker="o")

x = np.linspace(np.min((qn_a.min(), qn_b.min())), np.max((qn_a.max(), qn_b.max())))
plt.plot(x, x, color="k", ls="--")


plt.figure("122")
plt.plot(range(len(normalized_sp_log_returns)), normalized_sp_log_returns)
plt.plot(range(len(normalized_model_log_retruns)), normalized_model_log_retruns)

import seaborn as sns

plt.figure("123")
sns.distplot(normalized_model_log_retruns,label="model")
sns.distplot(normalized_sp_log_returns,label= "real")
plt.legend(loc="best")

plt.show()


from scipy import stats

# print(stats.ks_2samp(normalized_sp_log_returns, normalized_model_log_retruns,mode='asymp'))
# print(stats.ks_2samp(normalized_sp_log_returns, normalized_sp_log_returns))