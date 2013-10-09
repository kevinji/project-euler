'''
Problem 30

@author: Kevin Ji
'''

nums = []

# 2-digit nums
for a in range(1, 10):
    for b in range(0, 10):
        num = 10*a + b

        pow_a = 1
        pow_b = 1

        # Power of 5
        for _ in range(5):
            pow_a *= a
            pow_b *= b

        pow_num = pow_a + pow_b

        if num == pow_num:
            nums.append(num)

        # 3-digit nums
        for c in range(0, 10):
            num = 100*a + 10*b + c

            pow_c = 1

            # Power of 5
            for _ in range(5):
                pow_c *= c

            pow_num = pow_a + pow_b + pow_c

            if num == pow_num:
                nums.append(num)

            # 4-digit nums
            for d in range(0, 10):
                num = 1000*a + 100*b + 10*c + d

                pow_d = 1

                # Power of 5
                for _ in range(5):
                    pow_d *= d

                pow_num = pow_a + pow_b + pow_c + pow_d

                if num == pow_num:
                    nums.append(num)

                # 5-digit nums
                for e in range(0, 10):
                    num = 10000*a + 1000*b + 100*c + 10*d + e

                    pow_e = 1

                    # Power of 5
                    for _ in range(5):
                        pow_e *= e

                    pow_num = pow_a + pow_b + pow_c + pow_d + pow_e

                    if num == pow_num:
                        nums.append(num)

                    # 6-digit nums
                    for f in range(0, 10):
                        num = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f

                        pow_f = 1

                        # Power of 5
                        for _ in range(5):
                            pow_f *= f

                        pow_num = pow_a + pow_b + pow_c + pow_d + pow_e + pow_f

                        if num == pow_num:
                            nums.append(num)


print(nums)
print(sum(nums))
