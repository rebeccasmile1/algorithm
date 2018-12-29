"""
Description

合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""
import math
import sys

def merge(list, low, mid, high):
    left = list[low:mid]
    right = list[mid:high]
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    list[low:high]=result


def merge_sort():
    for line in sys.stdin:
        temp_list = line.split()
        if not temp_list:
            break
        data_list = []
        length = int(temp_list[0])
        for i in range(1, length + 1):
            data_list.append(int(temp_list[i]))

        # time=math.log(length,2)
        # for i in range(1,time+1):
        #     merge(e for e in data_list)

        i = 1
        while i < length:  # 子数组长度
            low = 0
            while low < length:
                mid = low + i
                high = min(mid + i, length)
                if mid<high:
                    merge(data_list,low,mid,high)
                low += 2 * i
            i *= 2
        s=''
        for e in data_list:
            s+=str(e)
            s+=' '
        print(s.strip())


if __name__ == '__main__':
    merge_sort()
