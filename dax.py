import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("Date-OHLC-Vol-dax-1m.csv", delimiter=';', parse_dates=[['Date', 'Time']], infer_datetime_format=True)

print(df.head())
print(df.info())

plt.figure()
plt.plot(df["Date_Time"], df["Close"])
plt.savefig("test.png")