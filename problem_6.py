'''
Problem 6

@author: Kevin Ji
'''

def get_sum_of_squares( num_terms ):
    return num_terms * ( num_terms + 1 ) * ( num_terms * 2 + 1 ) // 6

def get_square_of_sum( num_terms ):
    return ( num_terms * num_terms ) * ( ( num_terms + 1 ) * ( num_terms + 1 ) ) // 4

print( get_square_of_sum( 10 ) - get_sum_of_squares( 10 ) ) # 2640
print( get_square_of_sum( 100 ) - get_sum_of_squares( 100 ) )