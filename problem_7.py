'''
Problem 7

@author: Kevin Ji
'''

primes_list = [ 2, 3 ] # Cache list, will grow as get_nth_prime gets called

def get_nth_prime( term ):
    # Map term number to list index number (1 -> 0)
    term -= 1
    
    # If the index is less than the length of the list, then return the cached value
    if term < len( primes_list ):
        return primes_list[ term ]
    
    # Otherwise, get the last prime, add 2 for the next possible prime, and keep iterating from there
    test_prime = primes_list[ -1 ] + 2
    
    while len( primes_list ) <= term:
        # Flag determining whether test_prime is prime or not
        is_prime = True
        
        # See if it is divisble by any previous primes
        # If not, then test_prime must be prime
        for prime in primes_list:
            if test_prime % prime == 0:
                is_prime = False
                break
        
        # If it is prime, the flag should not have been switched
        if is_prime:
            primes_list.append( test_prime )
        
        # Increment by 2 to iterate through odd numbers
        test_prime += 2
    
    # Newest element must be the prime wanted
    return primes_list[ -1 ]

print( get_nth_prime( 6 ) ) # 13
print( get_nth_prime( 100 ) ) # 541
#print( primes_list )
print( get_nth_prime( 10001 ) )