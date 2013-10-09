'''
Problem 1

@author: Kevin Ji
'''

def get_sum_of_multiples( multiple, number ):
    num_multiples = number // multiple
    temp_sum = 0
    current_multiple = 1
    
    while current_multiple <= num_multiples:
        result = multiple * current_multiple
        temp_sum += ( result if result != number else 0 )
        current_multiple += 1
    
    return temp_sum

print( "10: " + str( get_sum_of_multiples( 3, 10 ) + get_sum_of_multiples( 5, 10 ) - get_sum_of_multiples( 15, 10 ) ) ) # 23
print( "1000: " + str( get_sum_of_multiples( 3, 1000 ) + get_sum_of_multiples( 5, 1000 ) - get_sum_of_multiples( 15, 1000 ) ) )