nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
  
# define bubble_sort():
def bubble_sort(arr):
    for el in arr:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
    return arr

print(bubble_sort(nums))
# [1, 2, 5, 5, 6, 9]