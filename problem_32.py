'''
Problem 32

@author: Kevin Ji
'''


def is_pandigital(multiplicand, multiplier, product):
    multiplicand_digits = []
    multiplier_digits = []
    product_digits = []

    while multiplicand > 0:
        new_digit = multiplicand % 10
        multiplicand_digits.append(new_digit)

        multiplicand //= 10

    while multiplier > 0:
        new_digit = multiplier % 10
        multiplier_digits.append(new_digit)

        multiplier //= 10

    while product > 0:
        new_digit = product % 10
        product_digits.append(new_digit)

        product //= 10

    # Now, look at all the ways that set of numbers could fail

    # Need 9 digits (1-9)
    if len(multiplicand_digits) + len(multiplier_digits) + len(product_digits) != 9:
        return False

    # No 0s
    if 0 in multiplicand_digits or 0 in multiplier_digits or 0 in product_digits:
        return False

    # Cannot duplicate digits
    if (len(multiplicand_digits) != len(set(multiplicand_digits)) or
            len(multiplier_digits) != len(set(multiplier_digits)) or
            len(product_digits) != len(set(product_digits))):
        return False

    # Now, test that all digits are in the three numbers
    for digit in range(1, 10):
        if (digit not in multiplicand_digits and digit not in multiplier_digits and
                digit not in product_digits):
            return False

    # Otherwise, we have all digits!
    return True

# is_pandigital tests
#print(is_pandigital(39, 186, 7254))  # True
#print(is_pandigital(76, 135, 6210))  # False

products = []

# Format: 1-digit x 4-digit = 4-digit
for multiplicand in range(1, 9):
    #print(multiplicand)

    for multiplier in range(1111, 9999):
        product = multiplicand * multiplier

        if product >= 10000:
            break

        if is_pandigital(multiplicand, multiplier, product):
            products.append(product)

# Format: 2-digit x 3-digit = 4-digit
for multiplicand in range(11, 99):
    #print(multiplicand)

    for multiplier in range(111, 999):
        product = multiplicand * multiplier

        if product >= 10000:
            break

        if is_pandigital(multiplicand, multiplier, product):
            products.append(product)

# Remove duplicates
products = list(set(products))
print(sum(products))
