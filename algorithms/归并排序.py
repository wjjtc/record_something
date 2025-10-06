B = []


def merge(A: list[int], low: int, high: int):
    mid: int = (low + high) // 2
    for k in range(low, high + 1):
        B[k] = A[k]
    i = low
    j = mid + 1
    k = i
    while i <= mid and j <= high:
        if B[i] <= B[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = B[j]
            j += 1
        k += 1
    while i <= mid:
        A[k] = B[i]
        k += 1
        i += 1
    while j <= high:
        A[k] = B[j]
        k += 1
        j += 1


def MergeSort(A: list[int], low: int, high: int):
    """
    归并排序（Merge Sort）
    
    这是一种高效的、基于“分治”（ Divide and Conquer ）思想的排序算法。
    它的核心思想是：
    1. 分（Divide）：递归地将当前数组对半切分，直到数组大小为1（天然有序）。
    2. 治（Conquer）：这一步在归并排序中是隐式的，因为大小为1的数组已经是“解决”好了的。
    3. 合（Combine）：将两个已经排好序的子数组合并（merge）成一个大的有序数组。
    """
    if low < high:
        mid: int = (low + high) // 2
        MergeSort(A, low, mid)
        MergeSort(A, mid + 1, high)
        merge(A, low, high)



A = [2,3,4,21,31,43,64,1,2,3,4,6,2,21]
B = [0] * len(A)
MergeSort(A,0,len(A)-1)

print(A)
