'''
描述

给定偶数（大于2），返回两个素数，其总和将等于给定数。有几种组合可能。仅打印第一对。

注意：解决方案将始终存在，请阅读Goldbach的猜想。同时，解决线性时间复杂度的问题，即O（n）。


输入

第一行包含T，即测试用例的数量。以下T行由每个数字组成，我们将为其找到两个素数。注意：该数字始终为偶数。


产量

对于每个测试用例，打印两个素数空格分开，使得较小的数字首先出现。每个测试用例的答案必须在一个新的行中。


样本输入1

5
74
1024
66
8
9990
样本输出1

3 71
3 1021
5 61
3 5
17 9973
'''
def prime(num):
    prime_list=[]

    for i in range(2,num):
        flag=True
        for j in range(2,i):
            if (i%j==0):
                flag=False
                break
        if flag:
            prime_list.append(i)
    s1=''
    flag=False
    for s in range(0,len(prime_list)):
        for t in range(0,len(prime_list)):
            if ((prime_list[s]+prime_list[t])==num):
                print(prime_list[s],prime_list[t])
                flag=True
                break
        if flag:
            break

if __name__ == '__main__':
    count = int(input())
    for i in range(count):
        prime(int(input()))