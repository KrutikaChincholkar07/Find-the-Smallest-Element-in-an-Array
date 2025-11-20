n = int(input("Enter number of elements: "))
arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

smallest = arr[0]

for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element:", smallest)
