'''
从一列数中筛除尽可能少的数，使得这些数字从左到右看是先增大再减小的


输入是一个数组，数值空格隔开

输出是筛选后的数组，空格隔开，如果有多重结果，则一行一个结果

1 2 4 7 11 10 9 15 3 5 8 6

1 2 4 7 11 10 9 8 6



'''


def MAX(LIS, len):
    LIS.sort()
    return LIS[-1]
def DoubleEndLIS(data_list, len):
    max = 0
    k = 0
    LIS = []  # LIS数组中存储的是 递增子序列中最大值最小的子序列的最后一个元素（最大元素）在array中的位置
    B = []  # 从左到右LIS中最长子序列中最大值最小的子序列的最后一个元素所在的位置,也就是0~i的数字序列中最长递增子序列的长度-1
    C = []  # 从右到左LIS中最长子序列中最大值最小的子序列的最后一个元素所在的位置,也就是len-1~i的数字序列中最长递增子序列的长度-1
    for i in range(0, len):
        LIS.append(0)
        B.append(0)
    LIS[0] = data_list[0]
    for i in range(1, len):
        left = 0
        right = B[k]
        while left <= right:
            mid = (left + right) // 2
            if data_list[i] < LIS[mid]:
                right = mid - 1
            else:
                left = mid + 1
        LIS[left] = data_list[i]
        if left > B[k]:
            B[k + 1] = B[k] + 1
            k = k + 1
    for i in range(0,k):
        B[i]=B[i]+1



    #从右往左
    for i in range(0, len):
        LIS[i]=0
        C.append(0)
    k=0
    LIS[0] = data_list[len-1]
    i=len-2
    while i>=0:

        left = 0
        right = i
        while left <= right:
            mid = (left + right) // 2
            if data_list[i] < LIS[mid]:#以当前的作为最长子序列边界的长度如果比mid为最长子序列边界的长度小，则直接比较mid左边的
                right = mid - 1
            else:
                left = mid + 1
        LIS[left] = data_list[i]
        if left > C[k]:
            C[k + 1] = C[k] + 1
            k = k + 1
        i=i-1

    for i in range(0,k):
        C[i]=C[i]+1

    for i in range(0,len):
        if (B[i]+C[i])>max:
            max=B[i]+C[i]
    return len-max+1



if __name__ == '__main__':
    temp_list = input().split(' ')
    data_list = []
    list = []
    for element in temp_list:
        data_list.append(int(element))
        list.append(int(element))
    len=len(data_list)
    res=DoubleEndLIS(data_list,len)
    print(res)

    # LIS = []
    # for i in range(0, len(data_list)):  # 记录当前元素作为最大元素的最长递增序列长度
    #     LIS.append(1)
    #     for j in range(0, i):
    #         if data_list[i] > data_list[j] and LIS[j] + 1 > LIS[i]:
    #             LIS[i] = LIS[j] + 1
    # res = MAX(LIS, len(data_list))
    # print(res)
