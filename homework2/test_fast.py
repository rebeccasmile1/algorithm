"""
Description

快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。


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
def fast_sort(list,left,right):
    if left > right:
        return
    i=left
    j=right
    temp=list[left]
    while i!=j:
        while list[j]>=temp and i<j:
            j-=1
        while list[i]<=temp and i<j:
            i+=1
        (list[i],list[j])=(list[j],list[i])
    #i==j
    (list[left],list[i])=(list[i],list[left])
    fast_sort(list,left,i-1)
    fast_sort(list,i+1,right)

def sort():
    for line in sys.stdin:
        temp_list=line.split()
        if not temp_list:
            break
        length=int(temp_list[0])
        data_List=[]
        for i in range(1,length+1):
            data_List.append(int(temp_list[i]))
        fast_sort(data_List,0,length-1)
        print(data_List)
if __name__ == '__main__':
    sort()