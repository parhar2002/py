num=int(input("Enter a Number :"))
a=0
b=1
c=0

for i in range(num):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
