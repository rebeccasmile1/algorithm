'''诡异的错误是，算64开销很大，问题在于，如何优化它
Description

Let's define a Series Whose recurrence formula is as follows :

C(n)= 3C(i-1) + 4C(i-2) + 5C(i-3) + 6C(i-4)

C(0)= 2

C(1)= 0

C(2)= 1

C(3)= 7

Now based on this Series a Matrix Mi,j of size nn is to be formed.The top left cell is(1,1) and the bottom right corner is (n,n). Each cell (i,j) of the Matrix contains either 1 or 0. If C( (i*j)^3 ) is odd, Mi,j is 1, otherwise, it's 0.Count the total number of ones in the Matrix.


Input

First Line Of the input will contain an integer 'T'- the number of test cases . Each of the next 'T' lines consists of an integer 'n'.-denoting the size of the matrix.

Constraints :

1 ≤ T ≤ 1000

1 ≤ n ≤ 1000


Output

For each test case, output a single Integer -the taste value fo the dish of size-n*n.


Sample Input 1

1
2
Sample Output 1

0
'''
import numpy as np
def cal_C(n:int):
    if n == 0:
        return 2
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 7
    else:
        return 3 * cal_C(n - 1) + 4 * cal_C(n - 2) + 5 * cal_C(n - 3) + 6 * cal_C(n - 4)


# def triple(n):
#     return n*n*n
# def is_odd(n):
#     if n%2!=0:
#         return True
#     return False
if __name__ == '__main__':
    cases=int(input())
    for c in range(0,cases):
        n=int(input())
        sum=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                # if is_odd(calC(triple(i*j))):
                if cal_C((i * j) * (i * j) * (i * j))%2==0:
                    continue
                else:
                    sum = sum + 1
        print(sum)




















