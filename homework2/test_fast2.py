def partition(nums, low, high):
    high_flag = True
    low_flag = False
    pivot = nums[low]
    while low < high and low < len(nums) and high < len(nums):
        if high_flag:
            if nums[high] < pivot:
                nums[low] = nums[high]
                high_flag = False
                low_flag = True
            else:
                high -= 1
        if low_flag:
            if nums[low] > pivot:
                nums[high] = nums[low]
                high_flag = True
                low_flag = False
            else:
                low += 1
    nums[low] = pivot
    print(low)
    return low


def quickSort(nums):
    arr = []
    low = 0
    high = len(nums) - 1
    if low < high:
        mid = partition(nums, low, high)
        if low < mid - 1:
            arr.append(low)
            arr.append(mid - 1)
        if mid + 1 < high:
            arr.append(mid + 1)
            arr.append(high)
        while arr:
            r = arr.pop()
            l = arr.pop()
            mid = partition(nums, l, r)
            if l < mid - 1:
                arr.append(l)
                arr.append(mid - 1)
            if mid + 1 < r:
                arr.append(mid + 1)
                arr.append(r)
    print(nums)

if __name__ == '__main__':
    data_list=[13,24,3,56,34,3,78,12,29,49,84,51,9,100]
    quickSort(data_list)