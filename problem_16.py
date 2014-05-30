'''
Problem 16

@author: Kevin Ji
'''

def sum_of_digits(number):
    digit_sum = 0
    
    while number:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum

print(sum_of_digits(2 ** 1000))
