'''
Problem 17
Done simply with math.

@author: Kevin Ji
'''

# Basic units
one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8

twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6

hundred = 7
thousand = 8

AND = 3

sum_from_1_to_9 = one + two + three + four + five + six + seven + eight + nine
sum_from_10_to_19 = ten + eleven + twelve + thirteen + fourteen + fifteen + sixteen + seventeen + eighteen + nineteen
sum_from_20_to_99 = sum_from_1_to_9 * 8 + 10 * (twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety)
sum_from_1_to_99 = sum_from_1_to_9 + sum_from_10_to_19 + sum_from_20_to_99
sum_from_100_to_999 = 900 * hundred + (900 - 9) * AND + 100 * sum_from_1_to_9 + sum_from_1_to_99 * 9
sum_of_1000 = one + thousand
sum_from_1_to_1000 = sum_from_1_to_99 + sum_from_100_to_999 + sum_of_1000

print("1-9: " + str(sum_from_1_to_9)) # 36
print("10-19: " + str(sum_from_10_to_19)) # 70
print("20-99: " + str(sum_from_20_to_99)) # 748
print("1-99: " + str(sum_from_1_to_99)) # 854
print()
print("1-1000: " + str(sum_from_1_to_1000))
