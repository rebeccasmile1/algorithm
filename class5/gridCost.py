'''
Description

Given a square grid of size n, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.

Note : It is assumed that negative cost cycles do not exist in input matrix.


Input

The first line of input will contain number of test cases T. Then T test cases follow . Each test case contains 2 lines. The first line of each test case contains an integer n denoting the size of the grid. Next line of each test contains a single line containing N*N space separated integers depecting cost of respective cell from (0,0) to (n,n).

Constraints:1<=T<=50，1<= n<= 50


Output

For each test case output a single integer depecting the minimum cost to reach the destination.


Sample Input 1

2
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
2
42 93 7 14
Sample Output 1

327
63


贪婪分析：是可以走上下左右方向的，用一个矩阵来记录是否走过，一个来记录权值，
然后每次从上下左右选一个最小的，且未访问的走
动态规划：最右下角的，是坐标或者上面来的，每次选取最小


1
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20


327
'''
import numpy as np
def gridCost(matrix,size):
    cost=0
    unvisited_temp=[[1 for j in range(size)] for i in range(size)]
    unvisited=np.array(unvisited_temp)
    i=0
    j=0
    while i<size-1 and j<size-1:
        matrix=np.dot(matrix,unvisited)
        minimun = -1
        unvisited[i][j] = 0
        if i == 0 and j == 0:
            minimun = min(matrix[i][j + 1],  matrix[i + 1][j])
            cost+=minimun
            if minimun == matrix[i][j + 1]:
                j+=1
            else:
                i+=1
        elif i == 0:
            minimun = min(matrix[i][j + 1], matrix[i + 1][j], matrix[i, j - 1])
            cost += minimun
            if minimun == matrix[i][j + 1]:
                j+=1
            elif minimun==matrix[i + 1][j]:
                i+=1
            else:#minimun==matrix[i][j-1]
                j-=1
        elif j == 0:
            minimun=min(matrix[i][j+1],matrix[i+1][j],matrix[i-1][j])
            cost += minimun
            if minimun==matrix[i][j+1]:
                j+=1
            elif minimun==matrix[i+1][j]:
                i+=1
            else:
                i-=1
        else:
            minimun = min(matrix[i][j+1],matrix[i+1][j],matrix[i-1][j],matrix[i][j-1])
            cost += minimun
            if minimun==matrix[i][j+1]:
                j+=1
            elif matrix[i+1][j]:
                i+=1
            elif matrix[i-1][j]:
                i-=1
            else:
                j-=1


    return cost+matrix[-1][-1]
if __name__ == '__main__':
    cases=int(input())
    result=[]
    for i in range(cases):
        size=int(input())
        data_temp=list(map(int,input().strip().split()))
        data_matrix_temp=[]
        for j in range(size):
            data_matrix_temp.append([])
            for c in range(size):
                data_matrix_temp[j].append(data_temp[j * size + c])
        data_matrix=np.array(data_matrix_temp)
        result.append(gridCost(data_matrix,size))
    for i in range(cases):
        print(result[i])






