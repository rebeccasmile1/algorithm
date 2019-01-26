c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))

'''
描述

巴布尔最喜欢的数字是17.他喜欢可以被17整除的数字。这次他做的是他取一个数字N并试图通过重新排列数字找到可以被17整除的最大数字。随着人数的增加，他对自己的任务感到困惑。因此，作为程序员，您必须帮助他完成任务。注意：如果通过重新排列数字不能将数字整除，则打印“不可能”。N可能有前导零。


输入

第一行输入包含一个整数T，表示测试用例的数量。每个下一个T行包含数字N.


产量

对于新行中的每个测试用例，打印所需的输出。


样本输入1

4
17
43
15
16
样本输出1

17
34
51
Not Possible
'''
from typing import List, Any


def str_sort(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i + 1:]):
            # print(str_sort(s[0:i] + s[i + 1:]))
            str_list.append(s[i] + j)
    return str_list

def rearrange():
    count=int(input())
    # temp_list=[]
    num_list=[]
    for i in range(count):
        temp_str=input()
        temp=int(temp_str)
        count_digits=[]

        if temp==0:
            num_list.append("Not Possible")
            continue

        if temp%17==0:
            num_list.append(temp)
            continue

        list1 = []
        for char in temp_str:
            count_digits.append(int(char))
        list1=str_sort(temp_str)
        flag=False
        for e in list1:
           if int(e)%17==0:
                num_list.append(int(e))
                flag=True
                break
        if flag==True:
            continue
        else:
            num_list.append("Not Possible")
            continue
    print(num_list)



if __name__ == '__main__':
    rearrange()




















