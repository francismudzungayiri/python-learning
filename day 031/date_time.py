import datetime as dt

now = dt.datetime.now()
year = now.year #returns the current year
month = now.month
week_day = now.weekday()

week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday'] 

print(f'Year: {year}, month: {month}, day: {week_days[week_day]}')