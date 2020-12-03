def quicksort(arr, l = None, r = None):
    l = 0
    r = len(arr)-1
    if l<r:
        pivot_index = partition(arr,l,r)
        quicksort(arr,l,pivot_index-1)
        quicksort(arr,pivot_index+1,r)
    return arr

def partition(arr,l,r):
    pivot_index = l
    small_part_boundary = pivot_index+1
    i = small_part_boundary
    while(i<=r):
        if arr[i] < arr[pivot_index]:
            swap(arr,i,small_part_boundary)
            small_part_boundary +=1
        i +=1
    swap(arr,pivot_index,small_part_boundary-1)
    return small_part_boundary - 1

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]


print(quicksort([3,2,1]))