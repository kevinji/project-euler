'''
Problem 3

@author: Kevin Ji
'''

def get_prime_factors( number ):
    prime_factors = []
    
    # Start with 2
    cur_factor = 2
    
    while number % cur_factor == 0:
        prime_factors.append( cur_factor )
        number = number // cur_factor
    
    # Start with 3, increment by 2
    cur_factor = 3
    
    while number != 1 and cur_factor < number:
        while number % cur_factor == 0:
            prime_factors.append( cur_factor )
            number = number // cur_factor
        
        cur_factor += 2
    
    if number != 1 or len( prime_factors ) == 0:
        prime_factors.append( number )
    
    return prime_factors

def get_unique_prime_factors( number ):
    prime_factors = get_prime_factors( number )
    unique_prime_factors = []
    
    for factor in prime_factors:
        if factor not in unique_prime_factors:
            unique_prime_factors.append( factor )
    
    return unique_prime_factors

print( get_unique_prime_factors( 13195 ) ) # [5, 7, 13, 29]
print( get_unique_prime_factors( 600851475143 ) )
