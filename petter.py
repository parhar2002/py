n=5
for i in range(n+1):
    print(""*(n-i)+"* "*i)
n=5
for i in range(n+1):
    print(" "*(n - i) +"*" * i)
n=5
for i in range(n):
    print(" "*(n-i)+"* "*i)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

num =1
for i in range(n):
    for j in range(n+1):
        print(num,end=" ")
        num +=1
    print()

for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()

num = 65
for i in range(n):
    for j in range(i+1):
        print(chr(num),end=" ")
        num+=1
    print()

for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()