import heapq

nums = [10, 5, 3, 7, 8, 12, 15, 24]	#3 5 7 8 10 12 15 24

k = int(input("몇 번째로 작은 수를 찾으시나요? :"))

def find_kth_smallest(nums, k):
  k = heapq.nsmallest(k, nums)
  return k[-1]		
  
print(find_kth_smallest(nums, k))
