# Divisors of a number
# n = int(input("Enter number: "))
import math
# O(n) -TC
def divisor(n):
    ls = []
    for i in range(1,n+1):
        if(n%i == 0):
            ls.append(i)
    ls.sort()
    return ls
# O(√n) - TC
def divisor2(n):
    ls = []
    sqrtn = int(math.sqrt(n)) + 1
    for i in range(1, sqrtn):
        if(n%i == 0):
            ls.append(i)
            if(n//i != i):
                ls.append(n//i)
    return sorted(ls)


# Prime Number
# Number as a factor 1 and itself, with exactly 2 factors

# Brute Force TC = O(n)
def prime(n):
    count = 0

    for i in range(1,n+1):
        if(n%i == 0):
            count+=1
        if(count > 2):
            return False
    return True
# TC = O(√n)
def prime2(n):
    count = 0
    i = 1
    while i*i<= n:
        if(n%i == 0):
            count+=1
            if(n//i!=i):
                count+=1
        if(count > 2):
            return False
        i+=1
    return True
    

# Euclidean Algorithm for GCD using Division

a = int(input("Enter n1: "))
b = int(input("Enter n2: "))

def gcd(a,b):
    while a > 0 and b > 0:
        if a>b: a = a%b
        else: b = b%a
    if a == 0: return b
    return a

print(gcd(a,b))