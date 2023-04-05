from decimal import Decimal, ROUND_05UP, ROUND_HALF_EVEN, ROUND_HALF_UP


number_1 = Decimal(7.5).quantize(Decimal("1"), ROUND_HALF_EVEN)
number_2 = Decimal(8.5).quantize(Decimal("1"), ROUND_HALF_UP)
number_3 = Decimal(9.5).quantize(Decimal("1"), ROUND_HALF_EVEN)
number_4 = Decimal(10.5).quantize(Decimal("1"), ROUND_05UP)

print(number_1)
print(number_2)
print(number_3)
print(number_4)
