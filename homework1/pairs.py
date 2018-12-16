'''
输入一个数组和一个数字，在数组中查找两个数，使得他们的和正好是输入的那个数字，统计这样两个数的对数

输入第一行是数组，每一个数字用空格隔开，第二行是和

输出这样的两数有几对

1 2 4 7 11 0 9 15
11

3

'''
if __name__ == '__main__':
    list=input().split(' ')
    fixed_sum=int(input())
    data_list=[]
    count=0
    for element in list:
        data_list.append(int(element))

    for i in range(0,len(data_list)):
        for j in range(i+1,len(data_list)):
            if data_list[i]+data_list[j]==fixed_sum:
                count=count+1

    print(count)

