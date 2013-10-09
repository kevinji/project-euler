'''
Problem 26

@author: Kevin Ji
'''

from decimal import *
#getcontext().prec = 100

EPSILON = 1e-10


def cycle(orig_denom):
    new_denom = Decimal(orig_denom)

    # Remove all factors of 2 and 5 from denom;
    # they do not affect the cycle length.
    while new_denom % 2 == 0:
        new_denom /= 2

    while new_denom % 5 == 0:
        new_denom /= 5

    # Any numbers with no cycle will have new_denom = 1
    if new_denom == 1:
        return 0

    # Otherwise, let us find the length of the cycle
    #frac = Decimal(1) / new_denom
    #print(frac)
    length = 1
    pow_of_10 = Decimal(1)
    denom = Decimal(9)

    numer = denom / new_denom
    #print(numer)

    # At one point, numer should be an integer
    #while abs(numer - round(numer)) > EPSILON:
    while numer != round(numer):
        length += 1
        pow_of_10 *= 10
        denom += 9 * pow_of_10

        numer = denom / new_denom
        #print(numer)

    return length

largest_num = 2
longest_cycle = 0

for cur_num in range(2, 1000):
    getcontext().prec = cur_num * 10
    cycle_len = cycle(cur_num)

    if cycle_len > longest_cycle:
        largest_num = cur_num
        longest_cycle = cycle_len

print(largest_num)
