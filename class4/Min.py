'''
最小化初始点
Description

Given a grid with each cell consisting of positive, negative or no points i.e, zero points.
We can move across a cell only if we have positive points ( > 0 ).
Whenever we pass through a cell, points in that cell are added to our overall points.
We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :

1.From a cell (i, j) we can move to (i+1, j) or (i, j+1).

2.We cannot move from (i, j) if your overall points at (i, j) is <= 0.

3.We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.


Input

The first line contains an integer 'T' denoting the total number of test cases.In each test cases, the first line contains two integer 'R' and 'C' denoting the number of rows and column of array.
The second line contains the value of the array i.e the grid, in a single line separated by spaces in row major order.

Constraints:

1 ≤ T ≤ 30

1 ≤ R,C ≤ 10

-30 ≤ A[R][C] ≤ 30

Input: points[m][n] =
{ {-2, -3, 3},
  {-5, -10, 1},
  {10, 30, -5}
};

1
3 3
-2 -3 3 -5 -10 1 10 30 -5

Output

Print the minimum initial points to reach the bottom right most cell in a separate line.

7

Explanation:
7 is the minimum value to reach destination with
positive throughout the path. Below is the path.

(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)

We start from (0, 0) with 7, we reach(0, 1)
with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)with and finally we have 1 point (we needed

x表示横轴 y表示纵轴，从(0,0)，到(m-1,n-1)
'''
def min():
    size=list(map(int,input().strip().split(' ')))
    data_matrix=[[0 for j in range(size[1])] for i in range(size[0])]
    data_list=list(map(int,input().strip().split(' ')))
    index=0
    for i in range(size[0]):
        for j in range(size[1]):
            data_matrix[i][j]=data_list[index]
            index+=1

    res_arr=count_partition(size[0]-1,size[1]-1)
    minmum=data_matrix[0][0]
    final_arr=[]
    for k in res_arr:
        count=data_matrix[0][0]
        i=0
        j=0
        for l in k:
            if l==1:
                i+=1
            else:
                j+=1
            count+=data_matrix[i][j]
            if count<minmum:
                minmum=count
        final_arr.append(minmum)
        minmum=data_matrix[0][0]
    final_arr.sort()
    perm(abs(final_arr[-1])+1)





    # print(data_matrix)
    # result=count_partition(size[0]-1,size[1]-1)
    # start=1
    # temp=0
    # temp+=start
    #我的思路是，把所有的路，走一遍，求得结果，在里面求最小值
    # for i in range(size[0]):
    #     for j in range(size[1]):
    #         temp+=
# def count_partition(x,y):
#     res=[]
#     for i in range(0,x):
#         res.append(1)
#     for i in range(0,y):
#         res.append(0)
#     res_arr=perm(res)
#     return res_arr
# def perm(l):
#     if len(l)<=1:
#         return
#     r=[]
#     for i in range(len(l)):
#         s=l[:i]+l[i+1:]
#         p=perm(s)
#         for x in p:
#             r.append(l[i:i+1]+x)
#     return r
def perm(l:list):
  # if(len(l)<=1 or type(l)==int):
  #   return [l]
  if type(l)==int:
      return [l]
  r=[]
  for i in range(len(l)):
    s=l[:i]+l[i+1:]
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
    cases=int(input())
    for c in range(cases):
        min()
