# 矩阵计算
# Description
#
# Let's define a Series Whose recurrence formula is as follows :
#
# C(n)= 3C(i-1) + 4C(i-2) + 5C(i-3) + 6C(i-4)
#
# C(0)= 2
#
# C(1)= 0
#
# C(2)= 1
#
# C(3)= 7
#
# Now based on this Series a Matrix Mi,j of size nn is to be formed.The top left cell is(1,1) and the bottom right corner is (n,n).
# Each cell (i,j) of the Matrix contains either 1 or 0. If C( (i*j)^3 ) is odd, Mi,j is 1,
# otherwise, it's 0.Count the total number of ones in the Matrix.
#
#
# Input
#
# First Line Of the input will contain an integer 'T'- the number of test cases . Each of the next 'T' lines consists of an integer 'n'.-denoting the size of the matrix.
#
# Constraints :
#
# 1 ≤ T ≤ 1000
#
# 1 ≤ n ≤ 1000
#
#
# Output
#
import math


def count_ci(max_num, array):
    array.append(2)
    array.append(0)
    array.append(1)
    array.append(7)
    if max_num > 4:
        for i in range(4, max_num + 1):#递归开销大，所以迭代
            array.append(array[i-1]*3 + array[i-2]*4 + array[i-3]*5 + array[i-4]*6)

if __name__ == '__main__':
    test_cases = int(input())
    for i in range(0, test_cases):
        length = int(input())
        max_num = int(math.pow(length*length, 3))
        table = []
        count_ci(max_num, table)
        odd_count = 0
        for j in range(1, length + 1):
            for k in range(1, length + 1):
                if table[int(math.pow(j*k, 3))]%2 != 0:
                    odd_count += 1
        print(odd_count)
