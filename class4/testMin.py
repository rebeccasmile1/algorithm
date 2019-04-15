# 最小化初始点
# Description
#
# Given a grid with each cell consisting of positive, negative or no points i.e, zero points.
# We can move across a cell only if we have positive points ( > 0 ).
# Whenever we pass through a cell, points in that cell are added to our overall points.
# We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
#
# 1.From a cell (i, j) we can move to (i+1, j) or (i, j+1).
#
# 2.We cannot move from (i, j) if your overall points at (i, j) is <= 0.
#
# 3.We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
#
#
# Input
#
# The first line contains an integer 'T' denoting the total number of test cases.In each test cases, the first line contains two integer 'R' and 'C' denoting the number of rows and column of array.
# The second line contains the value of the array i.e the grid, in a single line separated by spaces in row major order.
#
# Constraints:
#
# 1 ≤ T ≤ 30
#
# 1 ≤ R,C ≤ 10
#
# -30 ≤ A[R][C] ≤ 30
#
# Input: points[m][n] = { {-2, -3, 3},
# {-5, -10, 1},
# {10, 30, -5}
# };
#
#
# Output
#
# Print the minimum initial points to reach the bottom right most cell in a separate line.
#
# 7
#
# Explanation:
# 7 is the minimum value to reach destination with
# positive throughout the path. Below is the path.
#
# (0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)
#
# We start from (0, 0) with 7, we reach(0, 1)
# with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)with and finally we have 1 point (we needed

# x表示横轴 y表示纵轴
def perm(l):
    # print(l)
    if(len(l)<=1):
        return [l]
    r=[]
    for i in range(len(l)):
        s=l[:i]+l[i+1:]
        # print(s)
        p=perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
    return r


def count_partition(x,y):
    res = []
    for i in range(0,x):
        res.append(1)
    for i in range(0,y):
        res.append(0)
    res_arr = perm(res)
    return res_arr

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(0, test_cases):
        row,col = list(map(int, input().strip().split(' ')))
        matrix = [[0 for i in range(col)] for j in range(row)]
        matrix_info = list(map(int , input().strip().split(' ')))
        index = 0
        for i in range(0, row):
            for j in range(0, col):
                matrix[i][j] = matrix_info[index]
                index += 1
        res_arr = count_partition(row-1,col-1)
        min = matrix[0][0]
        final_arr = []
        for k in res_arr:
            count = matrix[0][0]
            i = 0
            j = 0
            for l in k:
                if l==1:
                    i += 1
                else:
                    j += 1
                count += matrix[i][j]
                if count < min:
                    min = count
            final_arr.append(min)
            min = matrix[0][0]
        final_arr.sort()
        print(abs(final_arr[-1]) + 1)





