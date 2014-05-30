'''
Problem 25

@author: Kevin Ji
'''

import math

def first_number_with_over_n_digits(digits):
    # Fibonacci terms
    prev_term = 1
    cur_term = 1
    
    term_num = 2
    
    while (int(math.log10(cur_term)) + 1) < digits:
        # Compute the next Fibonacci number
        next_term = prev_term + cur_term
        prev_term = cur_term
        cur_term = next_term
        
        term_num += 1
    
    return term_num

print(first_number_with_over_n_digits(1000))
