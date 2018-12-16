#单向
#LIS数组存储的是对应长度为i+1的最长子串的最小值，如LIS[3]=7,就是说当最长子串为4时，可以选数组里7这个数字
def getSub(arr,sub_len):
    index=0
    for i in range(0,len(arr)):
        index=index+1
        if index<sub_len:


# def MAX(LIS,len):
#     max=0
#     for i in range(0,len):
#         if LIS[i]>max:
#             max=LIS[i]
#     return max
# def LIS0(arr,len):
#     LIS=[1 for i in range(0,len)]
#     for i in range(0,len):
#         for j in range(0,i):
#             if arr[i]>arr[j] and LIS[j]+1>LIS[i]:
#                 LIS[i]=LIS[j]+1
#     res=MAX(LIS,len)
#     return res

def LIS(arr,len):#//LIS数组存储的是对应长度为i+1的最长子串的最小值，如LIS[3]=7,就是说当最长子串为4时，可以选数组里7这个数字
    LIS=[0 for i in range(0,len)]
    left=0
    right=0
    mid=0
    max=1
    LIS[0]=arr[0]
    for i in range(0,len):
        left=0
        right=max-1
        while left<=right:
            mid=(left+right)//2
            if LIS[mid]>=arr[i]:#每次是为了找i+1长度的最小值
                right=mid-1
            else:
                left=mid+1
        LIS[left]=arr[i]
        if left>=max:
            max+=1

    return max#在原来的里面去遍历，小于这个数的时候append到结果列表中去

if __name__ == '__main__':
    temp_list = input().split(' ')
    data_list = []
    list = []
    for element in temp_list:
        data_list.append(int(element))
        list.append(int(element))
    len = len(data_list)
    print(LIS(data_list,len))
    sub_len=LIS(data_list,len)