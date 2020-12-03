def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        pivot_index = partition(arr, left, right)
        quickSort(arr, left, pivot_index-1)
        quickSort(arr, pivot_index+1, right)
    return arr

def partition(arr, left, right):
    pivot_index = left
    small_part_boundary = pivot_index+1
    # it is like a placeholder for all items smaller than the left side pivot_index item
    i = small_part_boundary 
    while  i <= right:
        # traverse all items other than pivots
        if arr[i] < arr[pivot_index]:
            swap(arr, i, small_part_boundary)
            small_part_boundary+=1
        i+=1
    swap(arr,pivot_index,small_part_boundary-1)
    # push the pivot item to the middle 
    return small_part_boundary-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

print(quickSort([3,2,1]))