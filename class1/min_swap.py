'''
描述

给定N个不同元素A []的数组，找到排序数组所需的最小交换数。您需要完成函数，该函数返回一个整数，表示对数组进行排序所需的最小交换数。


输入

第一行输入包含一个整数T，表示测试用例的数量。然后是T测试案例。每个测试用例包含一个整数N，表示数组A []的元素。在下一行中是数组A []的N个空格分隔值。（1 <= T <= 100; 1 <= N <= 100; 1 <= A [] <= 1000）


产量

对于新行中的每个测试用例，输出将是一个整数，表示对数组进行排序所需的最小交换数量。

2
4
4 3 2 1
5
1 5 4 3 2

'''
def min_swaps(arr, n):
    hash_map = {val: index for index, val in enumerate(arr)}#enumerate是枚举，返回的是枚举
    swaps = 0
    sorted_arr = sorted(arr)#防止内部自排序了
    for i in range(n):
        if sorted_arr[i] != arr[i]:
            j = hash_map[sorted_arr[i]]#获得真正的在此位置上的数的下标
            arr[i], arr[j] = arr[j], arr[i]
            hash_map[arr[i]], hash_map[arr[j]] = i, j
            swaps += 1
    return swaps


if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_swaps(arr, n))