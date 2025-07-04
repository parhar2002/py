def sumd(n):
    return sum(int(digit)for digit in str(abs(n)))

num = int(input("Enter a Number: "))
print(f"Sum of digits: {sumd(num)}")
