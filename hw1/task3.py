# check if num is positive, negative, or 0
def checkNum(num):
    if (num > 0):
        print("num is positive")
    elif (num < 0):
        print("num is negative")
    else:
        print("num is zero")

# print the first 10 prime numbers
def primes():
    for num in range(2, 30):    # first 10 primes are all < 30
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# sum all numbers from 1 to 100
def sum():
    count = 0
    sum100 = 0

    while count < 100:
        count += 1
        sum100 += count
    
    print("Sum (1 to 100): " + str(sum100))

