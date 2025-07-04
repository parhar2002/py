num=int(input("Enter a number : "))
fact =1
for i in range(1,num+1):
    fact *=i

if num>0:
    print(f"{num} is {fact}")
else:
    print(f"{num} not a factorial")