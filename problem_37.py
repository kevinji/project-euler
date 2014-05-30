'''
Problem 37

@author: Kevin Ji
'''

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def is_truncatable_prime(number):
    # One-digit numbers do not count
    if number < 10:
        return False

    # Left-to-right: make a copy of number
    digits = len(str(number))
    ltr_number = number

    # Relies on num % 1 == 0
    while ltr_number > 0:
        if not is_prime(ltr_number):
            return False

        digits -= 1
        ltr_number %= 10**digits

    # Right-to-left: make a copy of number
    rtl_number = number

    while rtl_number > 0:
        if not is_prime(rtl_number):
            return False

        rtl_number //= 10

    # Otherwise, it is a truncatable prime
    return True


def is_prime(number):
    # 0 and 1 are not prime
    if number <= 1:
        return False

    # Use cached list first
    for prime in PRIMES:
        if prime * prime > number:
            return True

        if number % prime == 0:
            return False

    # Now, we test 6k-1 and 6k+1
    # 6(k-1) + 1 = 997 => k = 167
    k = 167

    # Only test to sqrt(number)
    while (6*k - 1) * (6*k - 1) <= number:
        if number % (6*k - 1) == 0 or number % (6*k + 1) == 0:
            return False

        k += 1

    # Otherwise, number must be prime
    return True


## Tests
# print(is_truncatable_prime(3797)) # True
# print(is_truncatable_prime(377)) # False
# print(is_truncatable_prime(7)) # False
#print(is_truncatable_prime(23)) # True

# Go up to 1000000
truncatable_primes = []

for number in range(1, 1000000, 2):
    if is_truncatable_prime(number):
        truncatable_primes.append(number)

print(truncatable_primes)
print(sum(truncatable_primes))
