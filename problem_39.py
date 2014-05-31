'''
Problem 39

@author: Kevin Ji
'''

import math

def is_square(number):
    return math.sqrt(number) % 1 == 0

def get_right_triangles(max):
    # Brute force right triangles
    right_triangles = {}

    for a in range(3, max + 1):
        for b in range(a + 1, max + 1):
            c_sq = a * a + b * b
            c = math.sqrt(c_sq)
            c_int = int(c)

            # Test if we have a right triangle
            if c_int * c_int == c_sq:
                perimeter = a + b + c_int

                if perimeter in right_triangles:
                    right_triangles[perimeter] += 1
                else:
                    right_triangles[perimeter] = 1

    return right_triangles


## Tests
right_triangles = get_right_triangles(500)
print(right_triangles)
print(max(iter(right_triangles.keys()), key=(lambda key: right_triangles[key])))
