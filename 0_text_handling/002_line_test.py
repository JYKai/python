import textwrap

long_text = "Life is too short, you need python. " * 10
line_text = textwrap.wrap(long_text, width=70)
line_fill_text = textwrap.fill(long_text, width=70)

print('\n'.join(line_text))
print(line_fill_text)
