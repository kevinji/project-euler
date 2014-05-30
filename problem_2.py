'''
Problem 2

@author: Kevin Ji
'''

def sum_even_fibonacci( max_value ):
    # Initial two elements
    prev_term = 1
    cur_term = 2
    temp_sum = 2
    
    while cur_term < max_value:
        next_term = prev_term + cur_term
        prev_term = cur_term
        cur_term = next_term
        
        if cur_term % 2 == 0:
            temp_sum += cur_term
    
    return temp_sum

print( sum_even_fibonacci( 4000000 ) )
