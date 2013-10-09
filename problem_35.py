'''
Problem 35

@author: Kevin Ji
'''

import collections
import itertools
import math

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def get_circular_primes_under(number):
    num_digits = math.floor(math.log10(number)) + 1
    circular_primes = set()
    non_circular_primes = set()

    # 2 and 5 are exceptions
    if number >= 2:
        circular_primes.add(2)
    
    if number >= 5:
        circular_primes.add(5)

    for digit_num in range(1, num_digits + 1):
        possible_primes_digits = itertools.product([1, 3, 7, 9], repeat=digit_num)
        # print(list(possible_primes_digits))

        for possible_prime_digits in possible_primes_digits:
            possible_circular_primes = get_digit_rotations(possible_prime_digits)
            # print(possible_circular_primes)
            all_prime = True
            cached = False

            # If smallest number in get_digit_rotations is too large, stop
            if min(possible_circular_primes) > number:
                break

            # All circular numbers must be prime
            for possible_circular_prime in possible_circular_primes:
                # Stop if prime is already cached in one of the sets
                if possible_circular_prime in circular_primes or possible_circular_prime in non_circular_primes:
                    cached = True
                    break

                if not is_prime(possible_circular_prime):
                    all_prime = False
                    break

            # Skip adding to the list if numbers are already cached
            if cached:
                continue

            if all_prime:
                circular_primes.update(possible_circular_primes)
            else:
                non_circular_primes.update(possible_circular_primes)

    return circular_primes


def get_number_rotations(number):
    digits = get_digits(number)
    return get_digit_rotations(digits)


def get_digits(number):
    digits = []
    number_copy = number

    while number_copy > 0:
        digits.append(number_copy % 10)

        number_copy //= 10

    return digits


def get_digit_rotations(digits):
    rotations = []
    digits_deque = collections.deque(digits)
    length = len(digits)

    # Rotate through all the digits
    for _ in range(length):
        rotations.append(get_number_from_digits(digits_deque))
        digits_deque.rotate(1)

    # Remove duplicates
    return set(rotations)


def get_number_from_digits(digits_deque):
    number = 0
    length = len(digits_deque)

    for digit_num in range(length):
        number *= 10
        number += digits_deque[digit_num]

    return number


def is_prime(number):
    # 0 and 1 are not prime
    if number <= 1:
        return False

    # Use cached list first
    for prime in PRIMES:
        if number % prime == 0:
            return False

        if prime * prime > number:
            return True

    # Now, we test 6k-1 and 6k+1
    # 6(k-1) + 1 = 997 => k = 167
    k = 167

    # Only test to sqrt(number)
    while (6*k-1) * (6*k-1) <= number:
        if number % (6*k - 1) == 0 or number % (6*k + 1) == 0:
            return False

        k += 1

    # Otherwise, number must be prime
    return True


# Tests
# print(get_number_from_digits(collections.deque([1, 2, 5])))
# print(get_digit_rotations([1, 7, 1]))
# print(get_digit_rotations([1, 1, 1]))

# circular_primes = get_circular_primes_under(100) # 13
circular_primes = get_circular_primes_under(1000000)

print(sorted(circular_primes))
print(len(circular_primes))

