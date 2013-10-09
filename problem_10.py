'''
Problem 10

@author: Kevin Ji
'''

import math

def is_prime( num ):
    test_factor = 3
    sqrt_limit = math.sqrt( num )
    
    while test_factor <= sqrt_limit:
        if num % test_factor == 0:
            return False
        
        test_factor += 2
    
    return True

def sum_of_primes_up_to( max_value ):
    # Sum of primes; default to 2 so we only increment the odds
    sum_of_primes = 2
    
    # Start our testing with 3
    test_prime = 3
    
    while test_prime < max_value:
        # DEBUG: Print out test_prime to see where we're at
        print( test_prime )
        
        # If test_prime is prime, add it to the sum_of_primes
        if is_prime( test_prime ):
            sum_of_primes += test_prime
        
        # Increment by 2 to iterate through odd numbers
        test_prime += 2
    
    # Return the sum_of_primes
    return sum_of_primes

print( sum_of_primes_up_to( 2000000 ) ) # 142913828922