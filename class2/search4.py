'''
描述

给定n个线性放置的磁体，每个磁体被视为点对象。每个磁体受到来自其左侧磁体的力，使得它们将其排斥到右侧，反之亦然。所有的力量都是令人厌恶的。力等于距离（1 / d，d是距离）。现在给出磁体的位置，找到沿着直线的所有点的任务，其中净力是零。

注意：距离必须以0.0000000000001的精度计算。

约束：1 <= T <= 100,1 <= N <= 100,1 <= M [] <= 1000


输入

第一行输入包含一个整数T，表示测试用例的数量。然后是T测试案例。每个测试用例的第二行包含整数N.然后在下一行中是数组M []的N个空格分隔值，表示磁体的位置。


产量

对于新行中的每个测试用例，打印空间分隔点，其净力为零，直到精确到两位小数。

2
2
1 2
4
0 10 20 30


1.50
3.82 15.00 26.18
'''
from  sympy import *
def search4():
    num=int(input())
    if num<1 or num>100:
        return
    for i in range(num):
        n=int(input())
        temp_list=input().split()
        points_list=[]
        for e in temp_list:
            if int(e)<1 or int(e)>1000:
                return
            points_list.append(int(e))
        if n<1 or n>100 or n!=len(temp_list):
            return
        result=[]
        s=points_list[0]
        for j in range(0,len(points_list)):
            f=(1/s+x)







if __name__ == '__main__':
    search4()