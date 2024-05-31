from collections import namedtuple

data = [
    ('홍길동', 23, '01011111111'),
    ('김철수', 31, '01022222222'),
    ('이영희', 29, '01033333333')
]

# namedtuple 자료형 생성
Employee = namedtuple('Employee', 'name, age, cellphone')

# data = [Employee(emp[0], emp[1], emp[2]) for emp in data]
data = [Employee._make(emp) for emp in data]

emp = data[0]
print(emp.name, emp.age, emp.cellphone) # 홍길동 23 01011111111
print(emp._asdict()) # {'name': '홍길동', 'age': 23, 'cellphone': '01011111111'}

# emp.name = '박길동' -> 값 변경시 오류 발생
new_emp = emp._replace(name='박길동')
print(new_emp) # Employee(name='박길동', age=23, cellphone='01011111111')
