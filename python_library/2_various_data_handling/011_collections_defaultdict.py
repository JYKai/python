from collections import defaultdict

text = 'Life is too short, You need python.'

text_dict = defaultdict(int)
for key in text:
    text_dict[key] += 1

print(text_dict) # defaultdict(<class 'int'>, {'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 
                 # 's': 2, 't': 3, 'o': 5, 'h': 2, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 2, 'd': 1, 'p': 1, 'y': 1, '.': 1})