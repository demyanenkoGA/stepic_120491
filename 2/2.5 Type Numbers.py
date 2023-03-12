"""
2.5 Числовые типы данных
"""

num_1 = 5
print(num_1)  # 5
print(type(num_1))  # <class 'int'>

# ---------------------------------------------

num_1 = 5
num_2 = 10
num_3 = 2
result_1 = num_1 + num_2
print(f'{num_1} + {num_2} = {result_1}')  # 5 + 10 = 15

result_2 = -(num_1 + num_2)
print(f'-({num_1} + {num_2}) = {result_2}')  # -(5 + 10) = -15

print('-'*10)

result_3 = num_1 - num_2
print(f'{num_1} - {num_2} = {result_3}')  # 5 - 10 = -5

result_4 = -(num_1 - num_2)
print(f'-({num_1} - {num_2}) = {result_4}')  # -(5 - 10) = 5

print('-'*10)

result_5 = num_1 * num_2
print(f'{num_1} * {num_2} = {result_5}')  # 5 * 10 = 50

result_6 = (num_1 * num_2) * 2
print(f'({num_1} * {num_2}) * 2 = {result_6}')  # (5 * 10) * 2 = 100

result_7 = num_3 * 2
print(f'{num_3} * 2 = {result_7}')  # 2 * 2 = 4

print('-'*10)

result_8 = num_3 ** 5
print(f'{num_3} ** 5 = {result_8}')  # 2 ** 5 = 32

print('-'*10)

num_1 = 50
num_2 = 8

result_9 = num_1 / num_2
print(f'{num_1} / {num_2} = {result_9}')  # 50 / 8 = 6.25
print(f'{num_1} / {num_2} = {int(result_9)}')  # 50 / 8 = 6

result_10 = num_1 // num_2
print(f'{num_1} // {num_2} = {result_10}')  # 50 // 8 = 6

print('-'*10)

result_11 = num_1 % num_2
print(f'{num_1} % {num_2} = {result_11}')  # 50 % 8 = 2


num_1 = 5
num_2 = 5
num_3 = 10
print(f'num_1 == num_2 - {num_1 == num_2}')  # num_1 == num_2 - True
print(f'num_3 == num_2 > {num_3 > num_2}')  # num_1 == num_2 - False

print('-'*10)

num_1 = float(10.5)
print(f'num_1 = {num_1}')  # num_1 = 10.5

num_2 = 10
result_12 = num_1 + num_2
print(f'{num_1} + {num_2} = {result_12}')  # 10.5 + 10 = 20.5

result_13 = int(num_1 + num_2)
print(f'{num_1} + {num_2} = {result_13}')  # 10.5 + 10 = 20
