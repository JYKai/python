# Text handling

<details>  
<summary>문자열을 줄여 표시하려면?</summary>  
<div markdown="1"> 

---

**textwrap.shorten()**
- 문자열을 원하는 길이에 맞게 줄여 표시(...)할 때 사용하는 함수

```python
import textwrap

text = "Life is too short, you need python"
k_text = "인생은 짧으니 파이썬이 필요해"

shorten_text = textwrap.shorten(text, width=15)
shorten_k_text = textwrap.shorten(k_text, width=15)

print(text) # Life is too short, you need python
print(shorten_text) # Life is [...]
print(shorten_k_text) # 인생은 짧으니 [...]
```

- 매개변수 width : 전달한 길이만큼 문자열을 줄여 표시
- 문자열에 포함된 모든 연속 공백은 하나의 공백 문자로 둘어든다.
- [...] 역시 전체 길이에 포함되며, 문자열은 단어 단위로 길이에 맞게 줄어든다.
- 한글 1문자를 길이 2가 아닌 1로 계산한다는 점에 주의하자.

```python
shorten_text = textwrap.shorten(text, width=15, placeholder='...')
print(shorten_text) # Life is too...
```
- 매개변수 placeholder : [...]를 ...로 변경하고 싶을 때 사용
---
</div> 
</details>



<details>  
<summary>긴 문장을 줄 바꿈하려면?</summary>  
<div markdown="1"> 

---
**textwarp.warp()**
- 긴 문자열을 원하는 길이로 줄 바꿈(warpping)할 때 사용하는 함수

```python
long_text = "Life is too short, you need python. " * 10

'''
Life is too short, you need python. Life is too short, you need python. Life is too 
short, you need python. Life is too short, you need python. Life is too short, you need
python. Life is too short, you need python. Life is too short, you need python. Life is 
too short, you need python. Life is too short, you need python. Life is too short, you 
need python.
''' 
```
```python
import textwrap

long_text = "Life is too short, you need python. " * 10
line_text = textwrap.wrap(long_text, width=70)
'''
['Life is too short, you need python. Life is too short, you need', 'python. Life is too
 short, you need python. Life is too short, you', 'need python. Life is too short, you 
need python. Life is too short,', 'you need python. Life is too short, you need python. 
Life is too', 'short, you need python. Life is too short, you need python. Life is', 'too 
short, you need python.']
'''
```
- textwrap.warp() 함수는 긴 문자열을 width 길이만큼 자르고 이를 리스트로 만들어 반환
  - 단어 단위로 문자열을 자르므로 단어 중간이 끊어지지 않는다.

```python
print('\n'.join(line_text))
'''
Life is too short, you need python. Life is too short, you need
python. Life is too short, you need python. Life is too short, you
need python. Life is too short, you need python. Life is too short,
you need python. Life is too short, you need python. Life is too
short, you need python. Life is too short, you need python. Life is
too short, you need python.
'''
```
- 하나의 문자열로 표시하고자 할 때, join() 함수로 문자열 사이에 줄 바꿈 문자(\n)를 넣어 출력

```python
line_text = textwrap.fill(long_text, width=70)
print(line_text)
'''
Life is too short, you need python. Life is too short, you need
python. Life is too short, you need python. Life is too short, you
need python. Life is too short, you need python. Life is too short,
you need python. Life is too short, you need python. Life is too
short, you need python. Life is too short, you need python. Life is
too short, you need python.
'''
```
- **textwrap.fill()** 함수를 사용하면 위 과정을 한 번에 진행할 수 있다. 
---
</div> 
</details>



<details>  
<summary>정규표현식으로 개인정보를 보호하려면?</summary>  
<div markdown="1"> 

---
**정규표현식(regular expression)**
- 복잡한 문자열을 처리할 때 사용하는 기법

**Use. 주민등록번호 뒷자리 처리**
- 정규표현식을 사용하지 않았을 때
 ```python
def not_re(data):
    result = []
    for line in data.split('\n'):
        word_result = []
        for word in line.split(' '):
            if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
                word = word[:6] + '-' + "*******"
            word_result.append(word)
        result.append(" ".join(word_result))

    print("\n".join(result))

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

not_re(data)
```

- 정규표현식을 사용했을 때

```python
import re

def use_re(data):
    pat = re.compile("(\d{6})[-]\d{7}")
    print(pat.sub('\g<1>-*******', data))

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

use_re(data)
```
- ```(\d{6})[-]\d{7}``` : 숫자6 + 붙임표(-) + 숫자7 (단, 숫자6은 괄호를 사용하여 그룹으로 지정했다.)
- ```\g<1>``` : 정규표현식과 일치하는 문자열 중 첫 번째 그룹을 의미한다.
- 정규표현식에서 그룹을 지정하려면 괄호로 묶으면 된다.
---

</div> 
</details>

<details>
<summary>Tips</summary>
<div markdown='1'>

---
1. 구두점을 간단하게 삭제하기
string 모듈의 punctuation에는 모든 구두점이 들어있다. 다음과 같이 strip 메서드에 string.punctuation을 넣으면 문자열 양쪽의 모든 구두점을 간단하게 삭제할 수 있다.
```python
import string

word = ', python.'
word.strip(string.punctuation + ' ')
```
- string.punctuation : '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
---
</div>
</details>
