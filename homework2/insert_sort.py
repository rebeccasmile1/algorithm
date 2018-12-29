"""
Description

实现插入排序。


Input

输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。


Output

输出排序的数组，用空格隔开，末尾不要空格。


Sample Input 1

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
"""
import sys
def insert_sort():
    for line in sys.stdin:
        temp_list=line.split()
        if not temp_list:
            break
        length=int(temp_list[0])
        data_list=[]
        for i in range(1,length+1):
            data_list.append(int(temp_list[i]))

        for i in range(1,length):
            x=data_list[i]
            for j in range(i,-1,-1):
                if x<data_list[j-1]:
                    data_list[j]=data_list[j-1]
                else:
                    break
            data_list[j]=x

        s=''
        for e in data_list:
            s+=str(e)
            s+=' '
        print(s.strip())






if __name__ == '__main__':
    insert_sort()