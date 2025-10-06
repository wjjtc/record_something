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
    """
    快速排序（Quick Sort）
    
    这同样是一种高效的、基于“分治”（Divide and Conquer）思想的排序算法。
    它通常是“原地排序”（in-place），意味着它不需要像归并排序那样占用额外的辅助数组空间。
    
    它的核心思想是：
    1. 分（Divide）：选择数组中的一个元素作为“基准”（Pivot）。然后，重新排列数组，
       使得所有小于基准的元素都移动到基准的左边，所有大于基准的元素都移动到右边。
       完成这一步后，该基准就处于其最终的排序位置。这个过程被称为“分区”（Partition）。
    2. 治（Conquer）：递归地对基准左边和右边的两个子数组进行快速排序。
    3. 合（Combine）：这一步在快速排序中是隐式的。因为分区操作是原地进行的，
       当递归调用结束时，整个数组就已经排好序了，不需要额外的合并步骤。
       """
    if low < high:
        tmp: int = partition(A, low, high)
        QuickSort(A, low, tmp - 1)
        QuickSort(A, tmp + 1, high)



A = [2,3,4,21,31,43,64,1,2,3,4,6,2,21]

QuickSort(A,0,len(A)-1)

print(A)