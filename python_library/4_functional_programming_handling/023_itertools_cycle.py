import itertools

emp_pool = itertools.cycle(['김지윤', '이윤지', '박지은'])
for _ in range(10):
    print(next(emp_pool), end=', ') # 김지윤, 이윤지, 박지은, 김지윤, 이윤지 ...   