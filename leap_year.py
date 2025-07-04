num = int(input("Enter a Year"))
if(num % 4 == 0)or(num %400==0):
    print(f"{num} is a leap year")
else:
    print(f"{num} not a leap year")