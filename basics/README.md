# Python Note

## 위치 인수
<details>
<summary>내용</summary>
<div markdown='1'>

---
함수에 인수를 순서대로 넣는 방식을 위치 인수라고 한다. 위치 인수를 사용하는 함수는 리스트(튜플) 앞에 *(애스터리스크)를 붙여서 리스트 언패킹으로 넣을 수 있다.

```python
def 함수이름(매개변수1, 매개변수2):    # 위치 인수를 사용하는 함수
    코드
 
함수(*리스트)    # 리스트 언패킹
함수(*튜플)      # 튜플 언패킹
```

위치 인수를 사용하는 가변 인수 함수는 매개변수 앞에 *를 붙여서 만든다.

```python
def 함수이름(*매개변수):    # 위치 인수를 사용하는 가변 인수 함수
    코드
 
함수(인수1, 인수2)    # 인수 여러 개를 직접 넣기
함수(*리스트)         # 리스트 언패킹
함수(*튜플)           # 튜플 언패킹
```
---
</div>
</details>

</br>

## 키워드 인수
<details>
<summary>내용</summary>
<div markdown='1'>

---
함수에 넣는 인수에 이름(키워드)를 붙이는 방식을 키워드 인수라고 한다. 키워드 인수는 딕셔너리 앞에 **(애스터리스크 두 개)를 붙여서 딕셔너리 언패킹으로 넣을 수 있다.

```python
함수(키워드1=값1, 키워드2=값2)     # 함수를 키워드 인수 방식으로 호출
 
함수(**딕셔너리)    # 딕셔너리 언패킹
```

키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만든다.

```python
def 함수이름(**매개변수):    # 키워드 인수를 사용하는 가변 인수 함수
    코드
 
함수(키워드1=값1, 키워드2=값2)    # 키워드 인수를 직접 넣기
함수(**딕셔너리)                  # 딕셔너리 언패킹
```
---
</div>
</details>

</br>

## 람다 표현식을 인수로 사용하기
<details>
<summary>내용</summary>
<div markdown='1'>

---
```python
list(map(lambda x: x + 10, [1, 2, 3])) # [11, 12, 13]
```

**이미지 파일만 가져오기**
```python
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('jpg') != -1 or x.find('png') != -1, files)))
```
- 문자열에서 find 메서드를 사용하면 찾을 문자열이 있을 때 인덱스를 반환하고 없을 때는 -1을 반환한다.
---
</div>
</details>

</br>

## 클로저
<details>
<summary>내용</summary>
<div markdown='1'>

---
클로저는 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가 함수를 호출할 때 다시 꺼내서 사용하는 함수를 뜻한다. 따라서 클로저는 **지역 변수와 코드를 묶어서 사용하고 싶을 때 활용**한다. 또한, 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용한다.

```python
def calc():    # calc 함수 안에 mul_add 함수를 만듦
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환 

c = calc()    # c에 저장된 함수가 클로저
print(c(1), c(2), c(3), c(4), c(5))    # 8 11 14 17 20
```
---
</div>
</details>

</br>

## 특정 클래스의 인스턴스인지 확인하기
<details>
<summary>내용</summary>
<div markdown='1'>

---
현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 ```isinstance``` 함수를 사용한다. 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환힌다.
```python
class Person:
     pass

james = Person()
isinstance(james, Person) # True, isinstance(인스턴스, 클래스)
```

```isinstance```는 주로 객체의 자료형을 판단할 때 사용한다. 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데, 실수와 음의 정수는 계산할 수 없다. 이런 경우에 ```isinstance```를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있다.
```python
def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)
```
---
</div>
</details>

</br>

## 비공개 속성 사용하기
<details>
<summary>내용</summary>
<div markdown='1'>

---
비공개 속성(private attribute): 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있는 속성
- 비공개 속성은 __속성과 같이 이름이 __(밑줄 두 개)로 시작해야 한다. 단, __속성__처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이 아니므로 주의해야 한다.

```python
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
```

```python
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000) # 이제 7000원 남았네요.
```
- 속성뿐만 아니라 메서드도 이름이 __(밑줄 두 개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 된다.

인스턴스와 클래스에서 \_\_dict__ 속성을 출력해보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있다.

```
>>> james.__dict__
{}
>>> Person.__dict__
mappingproxy({'__module__': '__main__', 'bag': ['책', '열쇠'], 'put_bag': <function Person.put_bag at 0x028A32B8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None})
```
---
</div>
</details>

</br>

## 클래스와 메서드의 독스트링 사용하기
<details>
<summary>내용</summary>
<div markdown='1'>

---
함수와 마찬가지로 클래스와 메서드도 독스트링을 사용할 수 있다.  

다음과 같이 클래스와 메서드를 만들 때 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개) 또는 ''' '''(작은따옴표 세 개)로 문자열을 입력하면 된다.  

그리고 클래스의 독스트링은 클래스.\_\_doc__ 형식으로 사용하고, 메서드의 독스트링은 클래스.메서드.\_\_doc__ 또는 인스턴스.메서드.\_\_doc__ 형식으로 사용한다.
```python
class Person:
    '''사람 클래스입니다.'''
    
    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')
 
print(Person.__doc__)             # 사람 클래스입니다.
print(Person.greeting.__doc__)    # 인사 메서드입니다.
 
maria = Person()
print(maria.greeting.__doc__)     # 인사 메서드입니다.
```
---
</div>
</details>

</br>

## 정적 메서드
<details>
<summary>내용</summary>
<div markdown='1'>

---
정적 메서드는 다음과 같이 메서드 위에 @staticmethod를 붙인다. 이때 정적 메서드는 매개변수에 self를 지정하지 않는다.
```python
class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드
```
- @staticmethod처럼 앞에 @이 붙은 것을 데코레이터라고 하며 메서드(함수)에 추가 기능을 구현할 때 사용한다.

```python
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출
```
- 정적 메서드를 호출할 때는 위와 같이 클래스에서 바로 메서드를 호출하면 된다.
- 정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없다. 그래서 보통 정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용한다.
- 정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수(pure function)를 만들 때 사용한다.
---
</div>
</details>

</br>

## 클래스 메서드
<details>
<summary>내용</summary>
<div markdown='1'>

---
클래스 메서드는 아래와 같이 메서드 위에 @classmethod를 붙인다.
```python
class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드
```

```python
class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.
```
이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 한다.

---
</div>
</details>