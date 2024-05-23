# Binary data handling
바이너리 데이터와 관련된 모듈 중 파이썬에서 C 구조체 바이너리 데이터를 사용하도록 하는 struct 모듈을 알아본다.

<details>  
<summary>C로 만든 데이터를 출력하려면?</summary>  
<div markdown="1"> 

---

**struct**
- C 언어로 만든 구조체 이진 데이터를 처리할 때 사용하는 모듈
- C 구조체로 만들어진 파일을 읽거나 네트워크로 전달되는 C 구조체 이진 데이터를 파이썬에서 처리할 때 주로 사용

```C
#include <stdio.h>
typedef struct
{
    double v;
    int t;
    char c;
} save_type;

int main()
{
    save_type s = {7.5f, 15, 'A'};
    FILE *f = fopen("output", "w");
    fwrite(&s, sizeof(save_type), 1, f);
    fclose(f);
    return 0;
}
```

```python
import struct

with open('output', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)
```
- unpack()
  - 'dicccc' : double형 1개, int형 1개, char형 4개를 뜻한다.
  - save_type 구조체는 double 1, int 1, char 1으로 이루어지지만 unpack()은 구조체 전체 길이가 16바이트 크기에 맞게 설정해야 한다. (double = 8, int = 4, char = 1, null = 3)

```python
struct.pack('dicccc', 7.5, 15, b'A', b'\x00', b'\x00', b'\x00')
```
- 이진 데이터를 생성할 때는 다음처럼 struct.pack()을 사용한다.
  - C 구조체의 char형 데이터를 생성하려면 포맷 문자 b를 이용하여 1바이트의 byte 문자열로 생성해야한다.
---

</div> 
</details>
