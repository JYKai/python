import datetime

day1 = datetime.date(2023, 10, 12)
print(day1) # 2023-10-12

day2 = datetime.date(2024, 5, 24)
print(day2) # 2024-05-24

diff = day2 - day1
print(diff.days) # 225

# 시, 분, 초까지 계산
day3 = datetime.datetime(2024, 5, 24, 11, 00, 00)
print(day3.hour) # 11
print(day3.minute) # 0
print(day3.second) # 0

# datetime.date 객체 + datetime.time 객체
day = datetime.date(2024, 5, 24)
time = datetime.time(11, 5, 40)

dt = datetime.datetime.combine(day, time)
print(dt) # 2024-05-24 11:05:40

day = datetime.date(2024, 5, 24)
print(day.weekday()) # 4