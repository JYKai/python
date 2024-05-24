def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

import calendar
print(calendar.isleap(0)) # True
print(calendar.isleap(4)) # True
print(calendar.isleap(700)) # False
print(calendar.isleap(1200)) # True
print(calendar.isleap(2024)) # True