'''
描述

给定一个整数数组，根据元素的频率对数组进行排序。例如，如果输入数组是{2,3,2,4,5,12,2,3,3,3,12}，则将数组修改为{3,3,3,3,2,2， 2,12,12,4,5}。如果两个元素的频率相同，则按递增顺序打印它们。


输入

第一行输入包含一个整数T，表示测试用例的数量。T测试案例的描述如下。每个测试用例的第一行包含一个表示数组大小的整数N. 第二行包含N个空格分隔的整数A1，A2，...，AN表示数组的元素。（1≤T≤70;30≤N≤130;1≤A[i]≤60）


产量

在单独的行中打印每个已排序的数组。



1
5
5 5 4 6 4

'''
def mycount():
    case_num=int(input())



    for i in range(0,case_num):
        result=[]
        data_num=int(input())
        list=input().split()
        data_list=[]
        # mydictionary = [[] for i in range(0, len(list))]  # mydictionary=[[] for i in range(0,61)]

        for j in list:
            data_list.append(int(j))

        mydictionary = []
        temp = 0
        mydictionary.append([])
        mydictionary[0].append(data_list[0])
        mydictionary[0].append(0)


        for num in data_list:
            flag=False
            for i in range(0,len(mydictionary)):
                if num==mydictionary[i][0]:#且等，则加1
                    mydictionary[i][1]+=1
                    flag=True
                    break
                else:#不等，则继续往下遍历
                    continue
            if flag==False:
                temp = temp + 1
                mydictionary.append([])
                mydictionary[temp] = []
                mydictionary[temp].append(num)
                mydictionary[temp].append(1)
            else:
                continue
        mydictionary.sort()
        mydictionary.sort(key=lambda x:x[1],reverse=True)
        for i in range(0,len(mydictionary)):
            for j in range(0,mydictionary[i][1]):
                print(mydictionary[i][0],end=' ')
                # result.append(mydictionary[i][0])
                # print(' '.join(str(mydictionary[i][0])))









if __name__ == '__main__':
    mycount()
    # case_num = int(input())
    #
    # for i in range(0, case_num):
    #     temp=[]
    #     result = []
    #     dict={}
    #     data_num = int(input())
    #     list = input().split()
    #     data_list = []
    #     for j in list:
    #         data_list.append(int(j))
    #         if j not in dict.keys():
    #             dict[j]=0
    #     data_list.sort()
    #     print(data_list)
    #     for key in data_list:
    #         dict[str(key)]+=1
    #     sorted(dict.items(),key=lambda x:x[1])#默认是降序
    #     print(dict)













