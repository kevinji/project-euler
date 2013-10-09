'''
Problem 36

@author: Kevin Ji
'''

def sum_of_palindromic_numbers_under(max_number):
    sum = 0

    for number in range(max_number):
        if is_palindrome(number, 10) and is_palindrome(number, 2):
            sum += number

    return sum

def is_palindrome(number, base=10):
    current_number = number
    reversed_number = 0

    while current_number > 0:
        units_digit = current_number % base
        reversed_number = reversed_number * base + units_digit
        current_number //= base

    return number == reversed_number


# Tests
# print(is_palindrome(10121, 10)) # False
# print(is_palindrome(13131, 10)) # True
# print(is_palindrome(1, 10)) # True
# print(is_palindrome(0, 10)) # True

# print(is_palindrome(33, 2)) # True
# print(is_palindrome(31, 2)) # True
# print(is_palindrome(29, 2)) # False

print(sum_of_palindromic_numbers_under(1000000))
