"""
Description

快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""
import sys


def partition(data_list, start, end):
    pivot = data_list[start]
    while start < end:
        while start < end and data_list[end] >= pivot:
            end -= 1
        data_list[start]=data_list[end]
        while start < end and data_list[start] <= pivot:
            start += 1
        data_list[end] = data_list[start]
        # (data_list[start],data_list[end])=(data_list[end],data_list[start])
    data_list[start] = pivot
    return start


def fast_sort():
    for line in sys.stdin:
        temp_list = line.split()
        if not temp_list:
            break
        length = int(temp_list[0])
        data_list = []
        for i in range(1, length + 1):
            data_list.append(int(temp_list[i]))

        stack = []
        stack.append(length - 1)
        stack.append(0)
        while stack:
            l = stack.pop()
            r = stack.pop()
            index = partition(data_list, l, r)
            if l < index - 1:
                stack.append(index - 1)
                stack.append(l)
            if r > index + 1:
                stack.append(r)
                stack.append(index + 1)
        s = ''
        for e in data_list:
            s += str(e)
            s += ' '
        print(s.strip())


if __name__ == '__main__':
    fast_sort()
