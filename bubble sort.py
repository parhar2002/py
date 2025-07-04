arr = [64,34,25,22,11]
n = len(arr)

for i in range(n):
    for j in range(n-1):

        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("Bubble sort array ",arr)