def quick_sort(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    return start
if __name__ == '__main__':
    arr=[13,24,3,56,34,3,78,12,29,49,84,51,9,100]
    quick_sort(arr)
    print(arr)