'''一开始的错因是，没有输出最大的；现在已经解决了
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

        for char in temp_str:
            count_digits.append(int(char))
        count_digits.sort(reverse=True)
        # print(count_digits)
        st=''
        for e in count_digits:
            st+=str(e)
        # print(st)
        list1=str_sort(st)
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
    s=''
    for e in num_list:
        print(e)



if __name__ == '__main__':
    rearrange()




















