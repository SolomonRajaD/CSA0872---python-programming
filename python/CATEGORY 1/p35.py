# Current time
from datetime import datetime
now=datetime.now()
print(now)

# Current date
from datetime import datetime
now=datetime.today()
print(now)

# Entire month in a year
import calendar
y = int(input("Enter the Year :"))
print(calendar.prcal(y))

# Particular month in a year
import calendar
y = int(input("Enter the Year :"))
m=int(input("Enter the month :"))
print(calendar.month(y,m))

#Program to find number of weekdays in(mm/yyyy)
import numpy as np
# Number of weekdays in March 2017
print("Number of weekdays in March 2017:",
      np.busday_count('2017-03', '2017-04'))

  
# Number of sundays in Nov 2020
print("Number of Sunday in november 2020:",
      np.busday_count('2020-11', '2020-12',weekmask='Sun'))
# input year and month
yearMonth = '2017-05'
  
# getting date of first monday
date = np.busday_offset(yearMonth, 0, roll='forward',weekmask='Mon')
# display date
print(date)
