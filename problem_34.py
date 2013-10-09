'''
Problem 34

@author: Kevin Ji
'''

FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


def factorial(number):
    return FACTORIALS[number]


def is_curious_num(number):
    temp_num = number
    curious_sum = 0

    while temp_num > 0:
        curious_sum += factorial(temp_num % 10)
        temp_num //= 10

    return number == curious_sum


# Tests
#print(is_curious_num(145))  # True
#print(is_curious_num(100))  # False

cur_sum = 0

for num in range(3, 1000000):
    if is_curious_num(num):
        cur_sum += num

print(cur_sum)
