#Pattern-1
def p1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
def p2(n):
    for i in range(n):
        print("*"*(i+1),end="")
        print()
def p3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end = "")
        print()
def p4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print()
def p5(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end = "")
        print() 
def p6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end = "")
        print()
def p7(n):
    for i in range(1,n+1):
          print(" "*(n-i),end = "")
          print("*"*(2*i-1),end = "")
          print(" "*(n-i))
def p8(n):
    for i in range(1,n+1):
        print(" "*(i-1), end = "")
        print("*"*(2*n-(2*i-1)), end = "")
        print(" "*(i-1))
def p9(n):
    p7(n)
    #p8(n-1)
    for i in range(1,n+1):
        if i==1:continue     
        print(" "*(i-1), end = "")
        print("*"*(2*n-(2*i-1)), end = "")
        print(" "*(i-1))
def p10(n):
    p2(n)
    p5(n-1)

def p11(n):
    start = 1
    for i in range(1,n+1):
        if(i%2==0): start = 0
        else: start = 1
        for j in range(i):
            print(start, end = " ")
            start = 1 - start
        print()
def p12(n):

    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end = "")
        print(" "*(2*n-2*i),end= '')
        for k in range(i,0,-1):
            print(k, end = "")
        print()
def p13(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end = " ")
            num+=1
        print()

def p14(n):
    alph = "ABCDEFGHIJKLMNO"
    for i in range(n):
        for j in range(i+1):
            print(alph[j], end = "")
        print()
def p15(n):
    alph = 'ABCDEFGHIJKLMNOP'
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print(chr(65+j), end=' ')
        print()
def p16(n):
    for i in range(n):
        print(chr(65+i)*(i+1))
def p17(n):
    for i in range(n):
        print(" "*(n-i-1), end = "")

        for j in range(i+1):
            print(chr(65+j),end = "")
        for k in range(i-1,-1,-1):
            print(chr(65+k), end = "")
        

        print(" "*(n-i-1))
def p18(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65 + (n-j-1)), end= " ")
        print()
def p19(n):
    for i in range(n):
        print("*"*(n-i), end = "")
        print(" "*(2*i), end = "")
        print("*"*(n-i), end = "")
        print()
    for i in range(n):
        print("*"*(i+1), end = "")
        print(" "*(2*n - 2*(i+1)), end = "")
        print("*"*(i+1))
def p20(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end = "")
        print(" "*(2*n - 2*(i+1)), end = "")
        print("*"*(i+1))
    for i in range(n):
        if(i==0): continue
        for j in range(n-i):
            print("*", end = "")
        print(" "*(i*2), end = "")
        print("*"*(n-i))
def p21(n):
    print("*"*n)
    for i in range(n-2):
        print("*", end = "")
        print(" "*(n-2), end = "")
        print("*", end = "\n")
    print("*"*n)
def p22(n):

    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            bottom = 2*n - 2 - i
            right = 2*n - 2 - j
            val = min(top, left, bottom, right)
            print(n-val, end = " ")
        print()

p2(11)