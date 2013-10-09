'''
Problem 31

@author: Kevin Ji
'''

num_ways = 0
currency_left = 200

for p200 in range(currency_left//200, -1, -1):
    currency_left = 200 - 200*p200

    for p100 in range(currency_left//100, -1, -1):
        currency_left = 200 - 200*p200 - 100*p100

        for p50 in range(currency_left//50, -1, -1):
            currency_left = 200 - 200*p200 - 100*p100 - 50*p50

            for p20 in range(currency_left//20, -1, -1):
                currency_left = 200 - 200*p200 - 100*p100 - 50*p50 - 20*p20

                for p10 in range(currency_left//10, -1, -1):
                    currency_left = 200 - 200*p200 - 100*p100 - 50*p50 - 20*p20 - 10*p10

                    for p5 in range(currency_left//5, -1, -1):
                        currency_left = 200 - 200*p200 - 100*p100 - 50*p50 - 20*p20 - 10*p10 - 5*p5

                        for p2 in range(currency_left//2, -1, -1):
                            currency_left = 200 - 200*p200 - 100*p100 - 50*p50 - 20*p20 - 10*p10 - 5*p5 - 2*p2

                            p1 = currency_left

                            num_ways += 1

print(num_ways)
