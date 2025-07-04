def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    year = int(input("Enter a Year: "))
    print(f"{year} is a leap year" if is_leap_year(year) else f"{year} is not a leap year")
except ValueError:
    print("Please enter a valid integer.")

try:
    year = int(input("Enter a Year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
except ValueError:
    print("Please enter a valid integer.")

