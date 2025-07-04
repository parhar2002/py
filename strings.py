name = "python"
print(len(name))
#-------------------
rev ="string"[::-1]
print(rev)
#-------------------
str= "javapoint"
str1=""
for i in str:
    str1=i+str1

print(str1)
#------------------------
string = "hello"
count = 0
for i in string:
    count+=1
print(count)
#--------------------------
countword = len("hello world in the sky ".split())
print(countword)
#------------------------------------
my_list = [5,9,7,2,6,8]
maximum = max(my_list)
minimum = min(my_list)
print("Maximum : ",maximum)
print("minimum : ",minimum)
#-------------------------------
my_list = [5,9,7,2,6,8]
lnum = None
lnum1 = None
for number in my_list:
    if lnum is None or lnum > number:
        lnum = number
    if lnum1 is None or lnum1 < number:
        lnum1=number

print("minimum",lnum)
print("miximum",lnum1)
#-------------------------------
num = int(input("Enter number : "))
total_sum=0
for i in range(1,num+1):
    total_sum= total_sum+i
print ("Total sum is ",total_sum)
#----------------------------------
string = "prohfdhjhbv"
result = ""
for char in string:
    if char not in result:
        result +=char
print(result)

string = "hello kjsdsk djskjdks ddskddsdsdw ew ew ewewe e"

str_len = 0
for char in string:
    str_len += 1

count = 1 if str_len > 0 else 0

for i in range(1, str_len):
    if string[i] == " " and string[i-1] != " ":
        count += 1
print(count)

s = "ACAACAAC"
result = [s[0]]
for char in s[1:]:
    if char != result[-1]:
        result.append(char)

print(''.join(result))
