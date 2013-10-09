'''
Problem 14

@author: Kevin Ji
'''

sequence_terms = {}
current_term = 0

def get_next_sequence_term():
    """Get the next term in the sequence that is defined by
    n -> n / 2 (n is even)
    n -> 3n + 1 (n is odd)
    
    Use a cached term if we reduce to a simpler case.
    """
    global current_term, sequence_terms
    current_term += 1
    
    number = current_term
    terms = 0
    
    # Try to reduce to a simpler version; else, use rules
    while number != 1 and number not in sequence_terms:
        terms += 1
        
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    
    if number in sequence_terms:
        terms += sequence_terms[ number ]
    
    # Allow for base case
    terms = terms if terms > 0 else 1
    
    sequence_terms[ current_term ] = terms
    return current_term

def longest_chain_below( number ):
    longest_chain_term = 1
    longest_chain = 1
    
    # Iterate all the way to number
    for unused in range( 0, number ):
        chain_term = get_next_sequence_term()
        chain = sequence_terms[ chain_term ]
        
        # Replace the stored longest chain if chain is larger
        if chain > longest_chain:
            longest_chain_term = chain_term
            longest_chain = chain
    
    return longest_chain_term

# TESTS
#for unused in range( 0, 13 ):
#    print( get_next_sequence_term() )

print( longest_chain_below( 1000000 ) )