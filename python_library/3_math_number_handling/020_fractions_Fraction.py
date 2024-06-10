from fractions import Fraction

a = Fraction(1, 5)
print(a) # 1/5

a = Fraction('1/5')
print(a) # 1/5

print(a.numerator) # 분자의 값 = 1
print(a.denominator) # 분모의 값 = 5

result = Fraction(1, 5) + Fraction(2, 5)
print(result) # 3/5
print(float(result)) # 0.6