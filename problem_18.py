'''
Problem 18

@author: Kevin Ji
'''

class TriangleSolver(object):
    '''
    Finds the largest total that can be constructed from a path in the triangle.
    '''
    
    def __init__(self, triangle):
        '''
        Constructor
        '''
        # Convert the triangle into an array.
        self.triangle_array = self.__convert_triangle_str_to_array(triangle)
    
    def __convert_triangle_str_to_array(self, string):
        '''
        Convert the triangle string to the equivalent array.
        '''
        # Create the array by splitting on newlines first
        array = string.split("\n")
        
        # Iterate through the array
        row_num = 0
        while row_num < len(array):
            # Now, split on spaces as well
            array[row_num] = array[row_num].split(" ")
            
            # Convert the strings to numbers
            array[row_num] = [int(num) for num in array[row_num]]
            
            row_num += 1
        
        return array
    
    def solve(self):
        '''
        Find the largest total possible.
        '''
        # Call the iterative solve function to get a total.
        total = self.__iter_solve(0, 0, 0)
        
        return total
    
    def __iter_solve(self, row_num, col_num, total):
        # Increment the total
        total += self.triangle_array[row_num][col_num]
        
        # Get the next row number.
        row_num += 1
        
        # Base: If we've reached the last row, end.
        if row_num == len(self.triangle_array):
            return total
        
        # Else, consider the two different routes.
        # Route 1: Go bottom.
        total_route_1 = self.__iter_solve(row_num, col_num, total)
        
        # Route 2: Go bottom and to the right.
        total_route_2 = self.__iter_solve(row_num, col_num + 1, total)
        
        # Return the largest of the two
        return total_route_1 if total_route_1 > total_route_2 else total_route_2

# Implementation
triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# Trim whitespace.
triangle = triangle.strip();

# Create a TriangleSolver
triangle_solver = TriangleSolver(triangle)

# Solve it.
largest_total = triangle_solver.solve()

print(largest_total)