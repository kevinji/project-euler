'''
Problem 9

@author: Kevin Ji
'''

def is_pythagorean_triple( a, b, c ):
    return True if ( a < b < c ) and ( a*a + b*b == c*c ) else False

def get_pythagorean_triplet( sum_of_triplet ):
    # a, b, c are the three values
    # a+b+c = sum_of_triplet
    a = 1
    b = 1
    c = 1
    
    a_limit = sum_of_triplet // 3
    b_and_c_limit = sum_of_triplet - a_limit
    b_limit = b_and_c_limit // 2
    
    while a <= a_limit:
        b_and_c_sum = sum_of_triplet - a
        b_limit = b_and_c_sum // 2
        
        b = 1
        
        while b <= b_limit:
            c = sum_of_triplet - a - b
            
            if is_pythagorean_triple( a, b, c ):
                return a, b, c
            
            b += 1
        
        a += 1
        
    return 0, 0, 0

def product_of_pythagorean_triplet( sum_of_triplet ):
    triplet = get_pythagorean_triplet( sum_of_triplet )
    return triplet[ 0 ] * triplet[ 1 ] * triplet[ 2 ]

#print( is_pythagorean_triple( 3, 4, 5 ) )
print( get_pythagorean_triplet( 12 ) ) # (3, 4, 5)
print( get_pythagorean_triplet( 1000 ) )
print( product_of_pythagorean_triplet( 1000 ) )
