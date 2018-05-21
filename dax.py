import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Date-OHLC-Vol-dax-1m.csv", delimiter=';', parse_dates=[['Date', 'Time']], infer_datetime_format=True, nrows=5000)

print(df.head())
print(df.info())


plt.figure()
plt.plot(df["Date_Time"], df["Close"])
plt.savefig("dax.png")

idx = df.groupby(df['Date_Time'].apply(lambda x: x.date()))['Date_Time'].idxmax()
latestDf = df.iloc[idx].copy()

plt.figure()
plt.plot(latestDf['Date_Time'].apply(lambda x: x.time()))
plt.savefig("closing_time.png")


def EMA( series, n ):
    ema = series.ewm( span = n ).mean()
    return( ema )


latestDf['EMA']=EMA(latestDf['Close'], 10)
print(latestDf.head())

plt.figure()
plt.plot(latestDf["Date_Time"], latestDf["Close"])
plt.plot(latestDf["Date_Time"], latestDf["EMA"])
plt.legend()
plt.savefig("EMA.png")



