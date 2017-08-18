#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def GCDivisor(n1, n2):
    n1Divisors = []
    n2Divisors = []
    for n in range(1,n1):
        if n1 % n == 0:
            n1Divisors.append(n)
        else:
            pass
    for n in range(1,n2):
        if n2 % n == 0:
            n2Divisors.append(n)
        else:
            pass
    CommonDivisors = list(set(n1Divisors).intersection(n2Divisors))
    return max(CommonDivisors)


#Exercise 2
#Write a function that returns prime numbers less than 121
def PrimesUnder121():
    PrimeNumbers = [2, 3, 5, 7, 11, 13, 17,
    19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
    61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
    107, 109, 113]
    return PrimeNumbers


def OtherLessEfficientPrimeFunction(n):
    Primes = []
    for x in range(1,n):
        CommonDivisors = []
        for m in range(1, (x-1)):
            if x % m == 0:
                CommonDivisors.append(m)
            else:
                pass
        if len(CommonDivisors) < 2:
            Primes.append(x)
        else:
            pass
    return Primes





def Primal(x):
    Primes = []
    for m in range(1, (x-1)):
        CommonDivisors = []
        if x % m == 0:
            CommonDivisors.append(x)
            if len(CommonDivisors) == 1:
                Primes.append(x)
    return Primes

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html
