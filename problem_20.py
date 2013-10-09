'''
Problem 20

@author: Kevin Ji
'''

def sum_of_digits(number):
    '''Sum the digits of a number by taking the last digit and continually
    dividing by 10.'''
    digit_sum = 0
    
    while number:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum

def factorial(number):
    factorial = 1
    
    cur_num = 2
    
    while cur_num <= number:
        factorial *= cur_num
        cur_num += 1
    
    return factorial

print(sum_of_digits(factorial(100)))