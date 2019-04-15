import sys
#import homework2.fast_sort为什么用不了
#倒数第K小是什么意思，就是第K小吗
def IntervalKthLow(lista:list,left:int,right:int,K:int):
    if right>(len(lista)-1) or left<0 or left>(len(lista)-1) or left>right:
        return

    listtemp=[]
    for i in range(left,right+1):#关注range和lista[:]
        listtemp.append(lista[i])
    fast_sort(listtemp)
    # print(listtemp)
    print(listtemp[K-1])








def partition(data_list, start, end):
    pivot = data_list[start]
    while start < end:
        while start < end and data_list[end] >= pivot:
            end -= 1
        data_list[start]=data_list[end]
        while start < end and data_list[start] <= pivot:
            start += 1
        data_list[end] = data_list[start]
        # (data_list[start],data_list[end])=(data_list[end],data_list[start])
    data_list[start] = pivot
    return start


def fast_sort(data_list):


    stack = []
    stack.append(len(data_list) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(data_list, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    s = ''
    for e in data_list:
        s += str(e)
        s += ' '
    # print(s.strip())
if __name__ == '__main__':
    listtemp=input().split()
    temp=input().split()
    K=int(input())
    lista=[]

    for e in listtemp:
        lista.append(int(e))
    left=int(temp[0])
    right=int(temp[1])
    IntervalKthLow(lista,left-1,right-1,K)#处理成下标