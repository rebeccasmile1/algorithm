'''
描述
注意：并非在A2中的，不一定在A1中出现
给定两个数组A1 []和A2 []，以这样的方式对A1进行排序，使得元素之间的相对顺序与A2中的相对顺序相同。对于A2中不存在的元素。最后按排序顺序附加它们。还给出了A2 []中的元素数量小于或等于A1 []中的元素数量，而A2 []具有所有不同的元素。

输入：A1 [] = {2,1,2,5,7,1,9,3,6,8,8} A2 [] = {2,1,8,3}输出：A1 [] = {2 ，2,1,1,8,8,3,5,6,7,9}

由于2 [...]首先出现2，所有出现的2s应该首先出现在A []中，然后所有出现的1都是1，因为1出现在A []中的2之后。接下来所有出现的8然后所有出现的3.最后我们打印A1 []中不存在于A2 []中的所有元素

约束条件：1≤T≤501≤M≤501≤N≤10且N≤M1≤A1[i]，A2 [i]≤1000


输入

第一行输入包含一个整数T，表示测试用例的数量。每个测试用例的第一行是M和N.M是A1中元素的数量，N是A2中元素的数量。每个测试用例的第二行包含M个元素。每个测试用例的第三行包含N个元素。


产量
按照另一个数组的定义的顺醋打印排序的数组


1
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3

'''

if __name__ == '__main__':
    case_num = int(input())
    for i in range(0, case_num):
        temp_data_num = input().split()
        numA = int(temp_data_num[0])
        numB = int(temp_data_num[1])
        temp_listA = input().split()
        temp_listB = input().split()
        listA = []
        listB = []
        result = []
        for e in temp_listA:
            listA.append(int(e))
        for e in temp_listB:
            listB.append(int(e))
        # for e in listB:
        #     for s in listA:
        #         if s==e:
        listA.sort()

        # 首先是把B建成一个字典，带权重，然后遍历A，将A做成一个二维数组，按第二个元素排序

        dictB = {}
        level=numB
        for s in range(0, numB):
            dictB[listB[s]] =level-s
        # print(dictB)


        dictionaryA=[[] for i in range(0,numA)]
        # print(dictionaryA)
        for t in range(0,numA):
            dictionaryA[t].append(listA[t])
            dictionaryA[t].append(0)
            if dictionaryA[t][0] in dictB.keys():
                dictionaryA[t][1]=dictB[dictionaryA[t][0]]

        dictionaryA.sort(key=lambda x:x[1],reverse=True)
        print(dictionaryA)
