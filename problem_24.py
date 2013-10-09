'''
Problem 24

@author: Kevin Ji
'''


# A math solution!
perm = ""

# There are 9!=362880 perms per every first digit,
# so 1st digit must be a 2.
perm += "2"
# Remaining: 1000000 - 2*362880 = 274240
# Digits left: 0, 1, 3, 4, ..., 9

# There are 8!=40320 perms per every second digit,
# so 2nd digit must be a 7.
perm += "7"
# Remaining: 274240 - 6*40320 = 32320
# Digits left: 0, 1, 3, ..., 5, 6, 8, 9

# There are 7!=5040 perms per every third digit,
# so 3rd digit must be an 8.
perm += "8"
# Remaining: 32320 - 6*5040 = 2080
# Digits left: 0, 1, 3, ..., 5, 6, 9

# There are 6!=720 perms per every fourth digit,
# so 4th digit must be a 3.
perm += "3"
# Remaining: 2080 - 2*720 = 640
# Digits left: 0, 1, 4, 5, 6, 9

# There are 5!=120 perms per every fifth digit,
# so 5th digit must be a 9.
perm += "9"
# Remaining: 640 - 5*120 = 40
# Digits left: 0, 1, 4, 5, 6

# There are 4!=24 perms per every sixth digit,
# so 6th digit must be a 1.
perm += "1"
# Remaining: 40 - 1*24 = 16
# Digits left: 0, 4, 5, 6

# There are 3!=6 perms per every seventh digit,
# so 7th digit must be a 5.
perm += "5"
# Remaining: 16 - 2*6 = 4
# Digits left: 0, 4, 6

# There are 2!=2 perms per every eighth digit,
# so 8th digit must be a 4.
perm += "4"
# Remaining: 4 - 1*2 = 2
# Digits left: 0, 6

# There are 1!=1 perms per every ninth digit,
# so 9th digit must be a 6
perm += "6"

# Thus, last digit must be a 0.
perm += "0"

print(perm)
