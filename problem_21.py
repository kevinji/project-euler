'''
Problem 20

@author: Kevin Ji
'''

import math


def sum_of_divisors(number):
    '''
    Sum of all the divisors of a number,
    not including that number itself.
    '''
    sum = 1

    cur_factor = 2
    max_factor = math.sqrt(number)

    while cur_factor <= max_factor:
        if number % cur_factor == 0:
            # Don't count the square root twice
            if number == cur_factor * cur_factor:
                sum += cur_factor
            else:
                sum += cur_factor + number // cur_factor

        cur_factor += 1

    return sum


def divisors_up_to(max_num):
    divisors = {}
    cur_num = 1

    while cur_num <= max_num:
        divisors[cur_num] = sum_of_divisors(cur_num)
        cur_num += 1

    return divisors


def sum_of_amicable_numbers(divisors_cache):
    sum_nums = 0
    list_amicable = []
    divisor_1 = 1

    while divisor_1 <= len(divisors_cache):
        if divisor_1 not in list_amicable:
            divisor_2 = divisors_cache[divisor_1]

            if divisor_2 <= len(divisors_cache):
                divisor_3 = divisors_cache[divisor_2]

                if divisor_1 == divisor_3 and divisor_1 != divisor_2:
                    list_amicable.append(divisor_1)
                    list_amicable.append(divisor_2)

                    sum_nums += divisor_1 + divisor_2

        divisor_1 += 1

    return sum_nums

divisors_cache = divisors_up_to(10000)
print(sum_of_amicable_numbers(divisors_cache))
