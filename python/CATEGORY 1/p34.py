from datetime import datetime
from dateutil import relativedelta

# get two dates
d1 = '17/7/1980'
d2 = '16/3/2007'

# convert string to date object
start_date = datetime.strptime(d1, "%d/%m/%Y")
end_date = datetime.strptime(d2, "%d/%m/%Y")

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)
print('Years, Months, Days between two dates is')
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')

delta.years
d3=d1.split('/')
d4=d2.split('/')
BY=int(d3[2])
JY=int(d4[2])

if(delta.years>=19 and BY%4==0):
    print("I m a lucky adult")
elif delta.years<19:
    print("I m aspiring to become adult")
    
if BY%4==0:
    print("Birth year is leap Year")
else:
    print("Birth year is not a leap

if JY%4==0:
    print("Joining year is leap Year")
else:
    print("Joining year is not a leap Year")

