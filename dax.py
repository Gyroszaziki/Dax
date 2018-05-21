import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Date-OHLC-Vol-dax-1m.csv", delimiter=';', parse_dates=[['Date', 'Time']], infer_datetime_format=True)

print(df.head())
print(df.info())


def EMA( series, n ):
    ema = series.ewm( span = n ).mean()
    return( ema )


df['EMA']=EMA(df['Close'], 35000)
print(df.head())


plt.figure()
plt.plot(df["Date_Time"], df["Close"])
plt.plot(df["Date_Time"], df["EMA"])
plt.legend()
plt.savefig("dax.png")