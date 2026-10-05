# Printing name 'n' times using recursion
n = int(input("Enter n: "))
def printn(i,n):
    if(i>n):
        return
    print("Zameer")
    printn(1,n-1)

# Print 1 to N
def print1ton(i,n):
    if(i>n):
        return
    print(i)
    print1ton(i+1,n)


# Print N to 1
def printnto1(i,n):
    if(i>n):
        return
    print(n)
    printnto1(i,n-1)

#Print 1 to N using backtracking
def print1tonb(i,n):
    if i<1:
        return
    print1tonb(i-1,n)
    print(i)
     
#Print N to 1 using backtracking
def printnto1b(i,n):
    if i>n:
        return
    printnto1b(i+1,n)
    print(i)

# Sum of 1 to N using parameterized recursion

def sumofn(n, sum = 0):
    if(n<1):
        print(sum)
        return
    sumofn(n-1, sum+n)

# Sum of 1 to N using functional recursion

def sumofnf(n):
    if n == 0:
        return 0
    return n + sumofnf(n-1)

# Factorial of N using functional recursion

def factn(n):
    if n == 1:
        return 1
    return n * factn(n-1)

 # Reverse an array using recursion
a = [1,2,3,4,5,6,7]
def swap(i,j):
    a[i], a[j] = a[j], a[i]
ln = len(a) - 1
def rev(f):
    if f > ln//2:
        return
    swap(f,ln-f)
    rev(f+1)

rev(0) 

#Check if given string is a palindrome
s = "MADAM"
ln =len(s)
def is_palindrome(i:int)-> bool:
    if i> ln//2:
        return True
    if s[i] != s[ln - i - 1]:
        return False
    return is_palindrome(i+1)

# Getting nth fibbonacii number
def fib(n):
    if n <=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(n))
    
        
