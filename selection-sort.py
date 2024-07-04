def selectionSort(arr, start):
  if start < len(arr)-1:
    minIndex = start     
    for i in range(start, len(arr)):
      if arr[i] < arr[minIndex]:
        minIndex = i
        
    arr[start], arr[minIndex] = arr[minIndex], arr[start]
    selectionSort(arr, start+1)
    
numbers = [64, 34, 25, 12, 22, 11, 90]

selectionSort(numbers, 0)

print(numbers)