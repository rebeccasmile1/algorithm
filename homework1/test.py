def MAX(LIS,len):
    max=0
    for i in range(0,len):
        if LIS[i]>max:
            max=LIS[i]
    return max
def LIS(data_list,len):#LIS是用于记录当前各元素作为最大元素的最长递增序列长度
    LIS=[]
    for i in range(0,len):
        LIS.append(0)
    for i in range(0,len):
        LIS[i]=1#设置当前元素data_list[i]作为最大元素的最长递增序列长度为1
        for j in range(0,i):
            if data_list[i]>data_list[j] and LIS[j]+1>LIS[i]:
                LIS[i]=LIS[j]+1

if __name__ == '__main__':
    for i in range(10,0,-1):#取不到0哦
        print(i)