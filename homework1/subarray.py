# # #
# '''
# 连续子数组，第一行是数组，第二行是num，求最大值减去最小值结果大于num的子数组的个数，O(n)
#
#
# 3 6 4 3 2
# 2
#
# 大于是4
# 小于等于是6
# '''
#
#
def getNum(arr, num):
    if arr == None or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    qmax.append(data_list[0])
    qmin.append(data_list[0])
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            while qmin and arr[qmin[-1]] >= arr[j]:#qmin维护的是从小到大的
                qmin.pop()
            qmin.append(j)
            while qmax and arr[qmax[-1]] <= arr[j]:#qmax维护的是从大到小
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] <= num:
                break
            j += 1
        #左边界移动之前先判断最小值 和 最大值队列中第一个是否为左边界 如果相等则移除
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        res += j - i
        i += 1
    return res
if __name__ == '__main__':
    list=input().split()
    num=int(input())
    data_list=[]
    for e in list:
        data_list.append(int(e))
    # data_list.sort()
    print(getNum(data_list,num))



# if __name__ == '__main__':
#     list=input().split()
#     num=int(input())
#     data_list=[]
#     for e in list:
#         data_list.append(int(e))
#     res=0
#     max = data_list[0]
#     min = data_list[0]
#
#     for i in range(0,len(data_list)):
#         j=i+1
#         max=data_list[i]
#         min=data_list[i]
#         while j<len(data_list):
#             if data_list[j]>max:
#                 max=data_list[j]
#             elif data_list[j]<min:
#                 min=data_list[j]
#             if abs(max-min)>num:
#                 res=res+1
#                 j=j+1
#             else:
#                 break
#         i=i+1
#
#     print(res)
#



if __name__ == '__main__':
    list=input().split()
    num=int(input())
    data_list=[]
    for e in list:
        data_list.append(int(e))
    res=0
    max = data_list[0]
    min = data_list[0]

    for i in range(0,len(data_list)):
        j=i+1
        max=data_list[i]
        min=data_list[i]
        while j<len(data_list):
            if data_list[j]>max:
                max=data_list[j]
            elif data_list[j]<min:
                min=data_list[j]
            if abs(max-min)>num:
                res=res+1
                j=j+1
            else:
                break
        i=i+1

    print(res)










