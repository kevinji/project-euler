'''
Problem 33

@author: Kevin Ji
'''

from fractions import Fraction


def canceling_frac_digits(numerator, denominator):
    # Extract digits from numerator and denominator
    numerator_digits = []
    denominator_digits = []
    new_numerator = numerator
    new_denominator = denominator

    while new_numerator > 0:
        new_digit = new_numerator % 10
        numerator_digits.append(new_digit)

        new_numerator //= 10

    while new_denominator > 0:
        new_digit = new_denominator % 10
        denominator_digits.append(new_digit)

        new_denominator //= 10

    intersection = set.intersection(set(numerator_digits), set(denominator_digits))

    # No repeated digits
    if not intersection:
        return []

    # 0 case (e.g. 10/30) considered trivial
    if intersection == set([0]):
        return []

    # Test if removal of intersection digits reduces fraction
    # e.g. 49/98 -> 4/8
    new_numerator_list = list(set(numerator_digits) - intersection)
    new_denominator_list = list(set(denominator_digits) - intersection)

    if not new_numerator_list or not new_denominator_list:
        return []

    new_numerator = new_numerator_list[0]
    new_denominator = new_denominator_list[0]

    if new_denominator == 0:
        return []

    # Test if fractions are equal
    if numerator * new_denominator != new_numerator * denominator:
        return []

    return [new_numerator, new_denominator, list(intersection)[0]]


def is_canceling_frac(numerator, denominator):
    return True if canceling_frac_digits(numerator, denominator) else False


# Tests
#print(is_canceling_frac(10, 30))  # False
#print(is_canceling_frac(49, 98))  # True

#print(canceling_frac_digits(49, 98))


fracs = []

for numer in range(10, 100):
    for denom in range(numer + 1, 100):
        #print(numer, denom)
        if numer < denom and is_canceling_frac(numer, denom):
            digits = canceling_frac_digits(numer, denom)

            new_numer = digits[0]
            new_denom = digits[1]

            fracs.append((new_numer, new_denom))

# Reduce duplicates
fracs = list(set(fracs))

print(fracs)

# Find product
product = Fraction(1, 1)

for frac in fracs:
    product *= Fraction(frac[0], frac[1])

print(product.denominator)
