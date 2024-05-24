import datetime

today = datetime.date.today()
print(today) # 2024-05-24

diff_days = datetime.timedelta(days=100)
print(diff_days) # 100 days, 0:00:00

# 100일 후
print(today + diff_days) # 2024-09-01

# 100일 전
print(today - diff_days) # 2024-02-14