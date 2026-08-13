arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = arr[i]
        j = i
        
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j = j - gap
            
        arr[j] = temp
        
    gap = gap // 2

print(arr)