"""
Description

实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""
import math
import sys


def sort_count():
    for line in sys.stdin:
        temp_list=line.split()
        if not temp_list:
            break
        length=int(temp_list[0])
        data_list=[]
        for i in range(1,length+1):
            data_list.append(int(temp_list[i]))
        count_list=[0 for i in range(0,length)]
        for i in range(0,length):
            for j in range(0,length):
                if data_list[j]<data_list[i]:
                    count_list[i]+=1
        # print(count_list)
        mydict=[[] for i in range(length)]
        for i in range(length):
            mydict[i].append(data_list[i])
            mydict[i].append(count_list[i])
        # print(mydict)
        mydict.sort(key=lambda x:x[1])
        # print(mydict)
        s=''
        for i in range(length):
            s+=str(mydict[i][0])
            s+=' '
        print(s.strip())



if __name__ == '__main__':
   sort_count()