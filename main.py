import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("data.csv")


df["Date"] = df["Date"].replace("-","/", regex=True)
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
df.set_index("Date", inplace=True)

df["Close/Last"] = df["Close/Last"].replace("$","", regex=True)
#df["Close/Last"] = df["Close/Last"].replace(".","", regex=False)
#df["Close/Last"] = df["Close/Last"].str.strip()
#df["Close/Last"] = df["Close/Last"].replace('', '0')
df["Close/Last"] = pd.to_numeric(df["Close/Last"], errors='coerce')
df["Close/Last"] = df["Close/Last"].astype(float)
df["Close/Last"] = df["Close/Last"].fillna(0)  # Replace NaN with 0

df["Weekly_Roll"] =df["Close/Last"].rolling(window=7).mean()

AAPL= df[df["Company"]== "AAPL"]
SBUX = df[df["Company"]=='SBUX']
MSFT = df[df["Company"]=='MSFT']
CSCO = df[df["Company"]=='CSCO']
QCOM = df[df["Company"]=='QCOM']
META = df[df["Company"]=='META']
AMZN = df[df["Company"]=='AMZN']
TSLA = df[df["Company"]=='TSLA'] 
AMD  = df[df["Company"]=='AMD']
NFLX = df[df["Company"]=='NFLX']
plt.figure(figsize=(10,6))
plt.plot(AAPL.index, AAPL["Weekly_Roll"])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45)

print(AAPL["Weekly_Roll"].head(10))


plt.xlabel("date")
plt.ylabel("closing prices")
plt.title("closing prices of AAPL")
plt.show()