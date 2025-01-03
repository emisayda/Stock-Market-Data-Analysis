import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("data.csv")


df["Date"] = df["Date"].replace("-","/", regex=True)
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')


df["Close/Last"] = df["Close/Last"].str.replace("$","").astype(float)
df['Open'] = df['Open'].str.replace('$', '').astype(float)
df['High'] = df['High'].str.replace('$', '').astype(float)
df['Low'] = df['Low'].str.replace('$', '').astype(float)

AAPL = df[df["Company"] =="AAPL"]
SBUX = df[df["Company"]=='SBUX']
MSFT = df[df["Company"]=='MSFT']
CSCO = df[df["Company"]=='CSCO']
QCOM = df[df["Company"]=='QCOM']
META = df[df["Company"]=='META']
AMZN = df[df["Company"]=='AMZN']
TSLA = df[df["Company"]=='TSLA'] 
AMD  = df[df["Company"]=='AMD']
NFLX = df[df["Company"]=='NFLX']

fig, axes = plt.subplots(5,2, figsize= (15,20))
axes = axes.flatten()


axes[0].plot(AAPL['Date'], AAPL['Close/Last'])
axes[0].set_title('Class AAPL')

axes[1].plot(SBUX['Date'], SBUX['Close/Last'])
axes[1].set_title('SBUX')

axes[2].plot(MSFT['Date'], MSFT['Close/Last'])
axes[2].set_title('MSFT')

axes[3].plot(CSCO['Date'], CSCO['Close/Last'])
axes[3].set_title('CSCO')

axes[4].plot(QCOM['Date'], QCOM['Close/Last'])
axes[4].set_title('QCOM')

axes[5].plot(META['Date'], META['Close/Last'])
axes[5].set_title('META')

axes[6].plot(AMZN['Date'], AMZN['Close/Last'])
axes[6].set_title('AMZN')

axes[7].plot(TSLA['Date'], TSLA['Close/Last'])
axes[7].set_title('TSLA')

axes[8].plot(AMD['Date'], AMD['Close/Last'])
axes[8].set_title('AMD')

axes[9].plot(NFLX['Date'], NFLX['Close/Last'])
axes[9].set_title('NFLX')

plt.tight_layout()
plt.show()

def doji(df, threshold=0.001):
    return abs(df["Close/Last"] - df["Open"]) <= threshold *  df["Open"]

def hammer(df):
    body = abs(df['Close/Last'] - df['Open'])
    lower_stick = df[['Open', 'Close/Last']].min(axis=1) - df['Low']
    upper_stick = df['High'] - df[['Open', 'Close/Last']].max(axis=1)
    return (lower_stick > body) & ( body> upper_stick)
def bullish_engulfing(df):
    prev_open= df["Open"].shift(1)
    prev_close= df["Close/Last"].shift(1)
    return (prev_open>prev_close) & (df["Close/Last"]>df["Open"]) & (df['Close/Last'] > prev_open) & (df['Open'] < prev_close)

results = []

for company, group in df.groupby('Company'):
    group = group.sort_values('Date').reset_index(drop=True)

group['Doji'] = doji(group)
group['Hammer'] = hammer(group)
group['Bullish Engulfing'] = bullish_engulfing(group)

patterns = group[group['Doji'] | group['Hammer'] | group['Bullish Engulfing']]

if not patterns.empty:
        patterns['Company'] = company
        results.append(patterns)

if results:
    final_results = pd.concat(results, ignore_index=True)
    print(final_results)



     