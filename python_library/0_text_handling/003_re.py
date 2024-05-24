import re

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

def use_re(data):
    pat = re.compile("(\d{6})[-]\d{7}")
    print(pat.sub('\g<1>-*******', data))

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

not_re(data)
use_re(data)
