def partition(A: list[int], low: int, high: int) -> int:
    tmp: int = A[low]
    while low < high:
        while A[high] >= tmp and low < high:
            high -= 1
        A[low] = A[high]
        while A[low] <= tmp and low < high:
            low += 1
        A[high] = A[low]
    A[low] = tmp
    return low


def QuickSort(A: list[int], low: int, high: int):
    if low < high:
        tmp: int = partition(A, low, high)
        QuickSort(A, low, tmp - 1)
        QuickSort(A, tmp + 1, high)



A = [2,3,4,21,31,43,64,1,2,3,4,6,2,21]

QuickSort(A,0,len(A)-1)

print(A)