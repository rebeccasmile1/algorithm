'''这题错了！！！！！！
两个序列，a，b，大小都n，值为任意整数，无序，要求，交换a，b元素，使得(序列a元素的和）与（序列b元素的和）差值最小
输入为两行，分别为两个数组，每个值空格隔开

输出变化后的两个数组元素和的差绝对值

100 99 98 1 2 3
1 2 3 4 5 40


96


SA，SB
SA-A+B,SB-B+A
则，SA-SB+2（B-A)

'''
def Swap2Balance(a,b,len):
    suma=sum(a)
    sumb=sum(b)
    diff=suma-sumb
    while diff!=0:
        besti=0
        bestj=0
        bestChange=0
        for i in range(0,len):
            for j in range(0,len):
                change=a[i]-b[j]
                if abs(diff-2*change)<abs(diff-2*bestChange):
                    besti=i
                    bestj=j
                    bestChange=change
        if bestChange==0:#差不能再缩小了
            return diff
        (a[besti],b[bestj])=(b[bestj],a[besti])
        suma=suma-bestChange
        sumb=sumb+bestChange
        diff=suma-sumb
    return  diff

if __name__ == '__main__':
    tempa=input().split()
    tempb=input().split()
    a=[]
    b=[]
    for e in tempa:
        a.append(int(e))
    for e in tempb:
        b.append(int(e))
    res=Swap2Balance(a,b,len(a))
    print(a,b)
    print(abs(sum(a)-sum(b)))









# if __name__ == '__main__':
#     temp_list = input().split(' ')
#     a = []
#     for element in temp_list:
#         a.append(int(element))
#     temp_list = input().split(' ')
#     b = []
#     for element in temp_list:
#         b.append(int(element))
#     a.sort()
#     b.sort()
#     # print(a)
#     # print(b)
#     flag=True
#     for index in range(0,len(a)):
#         if a[index]==b[index]:
#             continue
#         else:
#             flag=1-flag
#             # print(flag)
#             if(flag==True):
#                 (a[index],b[index])=(b[index],a[index])
#     # print(a)
#     # print(b)
#     suma =sum(a)
#     sumb=sum(b)
#     # print(suma)
#     # print(sumb)
#     print(abs(suma-sumb))




