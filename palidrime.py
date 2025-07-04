num = int(input("Enter a Number"))
num_str = str(num)

if num_str == num_str[::-1]:
    print(f"{num} is a palidrome Number")
else:
    print(f"{num} not a palidrome number")