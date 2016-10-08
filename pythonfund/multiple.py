a = [2,4,10,16]

def multiply(arr,multiplier):
    for num in range(0,len(arr)):
        arr[num] = arr[num] * multiplier

multiply(a,5)

print a
