'''
Problem 29

@author: Kevin Ji
'''

seq = []
num = 1  # Stored value of currently calculated value

for a in range(2, 100+1):
    num = a

    for b in range(2, 100+1):
        num *= a

        seq.append(num)

seq = list(set(seq))
print(len(seq))
