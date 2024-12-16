

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
           return True
    else:
        return False




def day_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month > 12 or month < 1:
        return 'Invalid inputs'
    
    if leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month -1]

year = int(input('ENTER YEAR \n'))
month = int(input('ENTER MONTH \n'))
days = day_in_month(year, month)
print(days)