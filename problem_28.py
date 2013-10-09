'''
Problem 28

@author: Kevin Ji
'''


# We have to move by 2, 4, 6, 8, etc. as we spiral out
diag_sum = 1
cur_element = 1
cur_row = 2

while cur_row <= 1000:
    for _ in range(4):
        cur_element += cur_row
        diag_sum += cur_element

    cur_row += 2

print(diag_sum)
