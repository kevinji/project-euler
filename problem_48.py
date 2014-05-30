'''
Problem 48

@author: Kevin Ji
'''

def self_power_with_mod(number, mod):
    product = 1

    for _ in range(number):
        product *= number
        product %= mod

    return product


MOD = 10000000000
number = 0

for power in range(1, 1000 + 1):
    number += self_power_with_mod(power, MOD)
    number %= MOD

print(number)
