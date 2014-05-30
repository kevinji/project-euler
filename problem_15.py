'''
Problem 15

@author: Kevin Ji
'''

def build_grid(length, width):
    '''Build the grid, length = x-dir, width = y-dir.'''
    
    paths = []
    
    for x_dimension in range(0, length):
        paths.append([])
        
        for _ in range(0, width):
            paths[x_dimension].append(None)
    
    return paths

def paths_through_point(paths, x, y):
    '''Return a recursive function consisting of sum of the top and left points.
    
    Will also store results into paths
    '''
    
    # Base cases
    # Cached
    if paths[x][y] is not None:
        return paths[x][y]
    
    # x or y == -1 (not in grid)
    if x == -1 or y == -1:
        return 0
    
    # Top-left corner
    if x == 0 and y == 0:
        # Cache the result
        paths[x][y] = 1
        return 1
    
    # Otherwise, recursively call, and store result to paths
    paths[x][y] = paths_through_point(paths, x - 1, y) + paths_through_point(paths, x, y - 1)
    
    return paths[x][y]

def paths_through_grid(length, width):
    # +1 needed because we have length + 1 _points_
    paths = build_grid(length + 1, width + 1)
    
    return paths_through_point(paths, length, width)

print(paths_through_grid(2, 2)) # 6
print(paths_through_grid(20, 20))
