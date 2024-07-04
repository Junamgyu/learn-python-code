def bubbleSort(arr, last):
  if last > 0:
    for i in range(1, last):
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
    bubbleSort(arr, last-1)
    
numbers = [64, 34, 25, 17, 22, 15, 90]

bubbleSort(numbers, len(numbers))

print(numbers)