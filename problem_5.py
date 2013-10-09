'''
Problem 5

@author: Kevin Ji
'''

def get_factor_repetitions( number ):
    # Data of form
    # factor => repetitions
    factor_repetitions = {}
    
    # Start with 2
    cur_factor = 2
    
    while number % cur_factor == 0:
        factor_repetitions[ cur_factor ] = factor_repetitions.get( cur_factor, 0 ) + 1
        number = number // cur_factor
    
    # Start with 3, increment by 2
    cur_factor = 3
    
    while number != 1 and cur_factor < number:
        while number % cur_factor == 0:
            factor_repetitions[ cur_factor ] = factor_repetitions.get( cur_factor, 0 ) + 1
            number = number // cur_factor
        
        cur_factor += 2
    
    if number != 1:
        factor_repetitions[ number ] = 1
    
    return factor_repetitions

def get_smallest_evenly_divisible( largest_divisor ):
    number = 1
    number_factors = {}
    divisor = 1
    
    # Get the list of divisors
    while divisor <= largest_divisor:
        factors = get_factor_repetitions( divisor )
        
        for factor in factors:
            if factors[ factor ] > number_factors.get( factor, 0 ):
                number_factors[ factor ] = factors[ factor ]
        
        divisor += 1
    
    # Now create the number
    for factor, num_times in number_factors.iteritems():
        for unused in range( 0, num_times ):
            number *= factor
    
    return number

print( get_smallest_evenly_divisible( 10 ) ) # 2520
print( get_smallest_evenly_divisible( 20 ) )