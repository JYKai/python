from decimal import Decimal

print(Decimal('0.1') * 3) # 0.3
print(Decimal('1.2') - Decimal('0.1')) # 1.1
print(float(Decimal('0.1') * Decimal('0.1'))) # 0.01