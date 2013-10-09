'''
Problem 27

@author: Kevin Ji
'''

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def is_prime(num):
    # 0 and 1 are not prime
    if num <= 1:
        return False

    '''
    # For this algorithm, 2 and 3 must be tested first
    if num % 2 == 0 or num % 3 == 0:
        # Of course, 2 and 3 themselves are prime
        if num == 2 or num == 3:
            return True
        else:
            return False
    '''

    # Use cached list first
    element_num = 0
    primes_len = len(PRIMES)
    prime = PRIMES[element_num]

    while element_num < primes_len and prime * prime <= num:
        if num % prime == 0:
            return False

        element_num += 1
        prime = PRIMES[element_num]

    if prime * prime > num:
        return True

    # Now, we test 6k-1 and 6k+1
    # 6(k-1) + 1 = 997 => k = 167
    k = 167

    # Only test to sqrt(num)
    while (6*k-1) * (6*k-1) <= num:
        if num % (6*k - 1) == 0 or num % (6*k + 1) == 0:
            return False

        k += 1

    # Otherwise, num must be prime
    return True

longest_a = 0
longest_b = 0
longest_n = 0

for a in range(999, -1000, -1):
    for b in range(999, -1000, -1):
        # Start with n=0
        n = 0
        quad = n*n + a*n + b

        # Break out of b loop if quad is already <= 1
        if quad <= 1:
            break

        while is_prime(quad):
            n += 1
            quad = n*n + a*n + b

        # n is actually 1 too large, but for comparison purposes,
        # it doesn't matter.
        if n > longest_n:
            longest_n = n
            longest_a = a
            longest_b = b

print(longest_a * longest_b)
