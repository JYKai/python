from datetime import date
from enum import IntEnum

class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_menu(input_data):

    menu = {
        Week.MONDAY: '김치찌개',
        Week.TUESDAY: '비빔밥',
        Week.WEDNESDAY: '된장찌개',
        Week.THURSDAY: '불고기',
        Week.FRIDAY: '갈비탕',
        Week.SATURDAY: '라면',
        Week.SUNDAY: '청국장'
    }

    return menu[input_data.isoweekday()]

print(get_menu(date(2024, 6, 4))) # 비빔밥
print(get_menu(date(2024, 6, 5))) # 된장찌개