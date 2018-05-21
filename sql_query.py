import csv
import pandas as pd
from sqlalchemy import create_engine
import datetime

startDay = "27/12/1999"
day = startDay

def str2date(day):
    dd = int(day[0:2])
    mm = int(day[3:5])
    yyyy = int(day[6:])
    date = datetime.date(yyyy, mm, dd)
    return date

def date2str(date):
    day = "%02d/%02d/%d"%(date.day, date.month, date.year)
    return day

def nextDay(date):
    date += datetime.timedelta(days=1)
    return date


data = create_engine('sqlite:///csv_database.db')


query = 'SELECT MAX("High") FROM "daxdata" WHERE "Date"= "%s"' % (day)
df = pd.read_sql_query(query, data)


i = 0

while i < 10:
    day = date2str(nextDay(str2date(day)))
    query = 'SELECT "Date",MAX("High") FROM "daxdata" WHERE "Date"= "%s"' % (day)
    nextrow = pd.read_sql_query(query, data)
    if not nextrow.get_value(0, 'Date') == None
    #    df = df.append(nextrow)
    i += 1

print (df)




