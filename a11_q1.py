import pandas as pd
from datetime import datetime,time,date

#1. date time object for jan 15 2012
dt1=pd.Timestamp('2012-01-15')
print(dt1)

# 2.specific date and time of 9:20pm
dt2=pd.Timestamp('2006-11-21 21:20')
print(dt2)

# 3.local date and time
dt3=pd.Timestamp.now()