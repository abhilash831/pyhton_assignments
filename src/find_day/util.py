import calendar

def find_day(month, day, year):
    day_number = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_number]
    return day_name.upper()