# 全为1的，最大子矩阵中1的个数
'''
1 0 1 1
1 1 1 1
1 1 1 0



'''
import sys


def MaxmalRectangle(matrix):
    h = []

    for i in range(0, len(matrix[0])):  # 列
        h.append(0)
    m = len(matrix)  # 行数
    n = len(matrix[0])  # 列数
    max = 0
    # mat=[]
    # for i in range(0,m):
    #     mat.append(matrix[i])

    for i in range(0, m):
        for j in range(0, n):
            if i == 0:
                h[j]=(matrix[i][j])
            else:
                if matrix[i][j] == 0:
                    h[j]=0
                else:
                    h[j]=(matrix[i - 1][j] + 1)
        temp=LargestRecArea(h)
        if temp>max:
            max = temp
    return max


def LargestRecArea(height):
    if len(height) == 0:
        return 0
    i = 1
    max = height[0]
    stack = []
    stack.append(0)
    while i < len(height) or (i == len(height) and len(stack) > 0):
        if i != len(height) and (len(stack) == 0 or height[i] >= height[stack[-1]]):
            stack.append(i)
            i=i+1
        else:#弹出栈中大的
            top = height[stack.pop()]
            if len(stack) > 0:
                currMax = top * (i - stack[-1] - 1)
            else:
                currMax = top * i
            if currMax>max:
                max=currMax
        # print(stack)
    return max

if __name__ == '__main__':
    matrix = []
    temp_list = []
    max = 0

    while True:

        row = []
        temp_list = input().split()
        if not temp_list:
            break
        # print(temp_list)
        for e in temp_list:
            row.append(int(e))
        matrix.append(row)

    print(matrix)
    print(MaxmalRectangle(matrix))
