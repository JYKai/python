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
