import datetime

# a = '2000-11-21'
# x = datetime.date.today()
# two_weeks = (datetime.timedelta(days=14) + datetime.datetime.today()).date()
# y = datetime.datetime.strptime(a, "%Y-%m-%d").date()
# print(x)
# print(two_weeks)
# print(y)


dates = ['2020-02-01', '2000-02-15','1989-12-12','2020-03-20']
bdays = []
today = (datetime.datetime.today()).date()
two_weeks = (datetime.timedelta(days=14) + datetime.datetime.today()).date()
for item in dates:
    bdays.append(datetime.datetime.strptime(item, "%Y-%m-%d").date())
print(dates)   
print('hello')
print(bdays) 
print(bdays[0], bdays[1], bdays[2], bdays[3])
print('TEST')