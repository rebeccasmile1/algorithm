'''
时间复杂度好的算法,线性时间O(n)

2,5,3,0,2,3,0,3
'''
# -*- coding: utf-8 -*-

def countSort(data):
    i = 0;
    # 这里需要将使res的长度是data的长度加1，因为前面记录的是个数，不是下标
    result = [0] * (len(data) + 1)
    temp = [0] * (max(data) + 1)
    for i in range(len(data)):
        temp[data[i]] = temp[data[i]] + 1

    for i in range(len(temp)-1):
        temp[i+1] += temp[i]


    for i in range(len(data)):
        result[temp[data[i]]] = data[i]
        temp[data[i]] -= 1
        i -= 1

    print(result[1:])

data = [7, 5, 3, 0, 2, 3, 0, 3,11,1]
countSort(data)

