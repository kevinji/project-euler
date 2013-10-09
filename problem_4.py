'''
Problem 4

@author: Kevin Ji
'''

def is_palindrome( string ):
    if len( string ) == 0 or len( string ) == 1:
        return True
    
    if string[ 0 ] != string[ -1 ]:
        return False
    
    return is_palindrome( string[ 1 : -1 ] )

def get_largest_palindrome_from_product( num_digits ):
    smallest_number = 10 ** ( num_digits - 1 )
    largest_number = ( 10 ** num_digits ) - 1
    largest_palindrome = 0
    
    # Start iterating from smallest_number
    first_number = smallest_number
    
    while first_number <= largest_number:
        second_number = smallest_number
        
        while second_number <= largest_number:
            product = first_number * second_number
            
            if is_palindrome( str( product ) ) and product > largest_palindrome:
                largest_palindrome = product
            
            second_number += 1
        
        first_number += 1
    
    return largest_palindrome

print( get_largest_palindrome_from_product( 2 ) ) # 9009
print( get_largest_palindrome_from_product( 3 ) )