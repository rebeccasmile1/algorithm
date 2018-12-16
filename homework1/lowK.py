'''
#找到给定数组的给定区间的倒数第k小的数值
#第一行是数组，第二行是区间（两头都包含），两值用空格隔开，第三行是K值
1 2 3 4 5 6 7
3 5
2
'''
if __name__ == '__main__':
    list=input().split(' ')
    data_list=[]
    for element in list:
        data_list.append(int(element))
    list=input().split()
    src=int(list[0])
    dst=int(list[1])
    k=int(input())
    sub_list=[]
    for index in range(src-1,dst):
        sub_list.append(data_list[index])
    sub_list.sort()#从小到大排
    print(sub_list[k-1])


