import math
from random import randint
number1 = int(randint(1, 1000))
print(f'Первое задуманное число: {number1}')
number2 = int(randint(1, 1000))
print(f'Второе задуманное число: {number2}')
sum_of_numbers = number1+number2
print(f'Сумма двух задуманных чисел {sum_of_numbers}')
multi_of_numbers = number1*number2
print(f'Произведение двух задуманных чисел {multi_of_numbers}')
dis = sum_of_numbers*sum_of_numbers-4*multi_of_numbers
result1 = int((sum_of_numbers+math.sqrt(dis))/2)
result2 = int(multi_of_numbers/result1)
print(f'Первое задуманное число: {result1}')
print(f'Второе задуманное число: {result2}')
