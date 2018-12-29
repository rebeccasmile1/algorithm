"""
Description

实现冒泡排序。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""
import sys
def bubble():
    for line in sys.stdin:
        temp_list=line.split()
        if not temp_list:
            break
        length=int(temp_list[0])
        data_list=[]
        for i in range(1,length+1):
            data_list.append(int(temp_list[i]))
        for i in range(0,length):#把大的往后
            for j in range(0,length-i-1):#每次最大的在最后，且不哟名走到最后一个
                if data_list[j]>data_list[j+1]:
                    (data_list[j],data_list[j+1])=(data_list[j+1],data_list[j])
        #这样最后一个会有空格
        # for e in data_list:
        #     print(e,end=' ')
        s=''
        for e in data_list:
            s+=str(e)
            s+=' '
        print(s.strip())


if __name__ == '__main__':
    bubble()


