n=5
for i in range(n+1):
    print(""*(n-i)+"* "*i)

n = 5
for i in range(n+1):
    print(" "*(n - i) +"*" * i)


n = 5
for i in range(n+1):
    print(" "*(n - i) +"* " * i)

n = 5
for i in range(n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

n = 5
num = 1
for i in range(n):
    for j in  range(i + 1):
        print(num, end=" ")
        num += 1
    print()

n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i),end=" ")
    print()
    
n = 5
num = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(num), end=" ")
        num += 1
    print()

n = 5
for i in range(n):
    print(" " * (n-i-1),end="")
    for j in range(i+1):
        print(chr(65 + j), end=" ")
    print()
