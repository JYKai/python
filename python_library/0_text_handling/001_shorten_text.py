import textwrap

text = "Life is too short, you need python"
k_text = "인생은 짧으니 파이썬이 필요해"

shorten_text = textwrap.shorten(text, width=15)
shorten_k_text = textwrap.shorten(k_text, width=15)

print(text) # Life is too short, you need python
print(shorten_text) # Life is [...]
print(shorten_k_text) # 인생은 짧으니 [...]

shorten_text = textwrap.shorten(text, width=15, placeholder='...')
print(shorten_text) # Life is too...
