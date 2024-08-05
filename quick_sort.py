def Partition(arr,s,e):
  pivot = arr[s]
  i,j = s,e
  while i<j:
    while i<e and arr[i]<=pivot:
      i+=1
    while j>s and arr[j]>=pivot:
      j-=1
    if i<j:
      arr[i],arr[j] = arr[j],arr[i]
  arr[s],arr[j] = arr[j],arr[s]
  return j

def QuickSort(arr,s,e):
  if s>=e:
    return
  p = Partition(arr,s,e)
  QuickSort(arr,s,p-1)
  QuickSort(arr,p+1,e)

arr = [int(i) for i in input("Enter list : ").split()]
QuickSort(arr, 0, len(arr)-1)
print("Sorted list :",*arr)