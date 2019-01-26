'''
审错题了

描述

Archana非常喜欢弦乐。她喜欢解决许多与弦乐有关的问题。她遇到了一个她无法解决的问题。帮她解决。问题如下：-Given是一个长度为L的字符串。她的任务是从给定的字符串中找到最长的字符串，字符按照ASCII码的降序和算术级数排列。她希望公共差异应尽可能低（至少为1），并且字符串的字符应具有更高的ASCII值。


输入

第一行输入包含一个整数T，表示测试用例的数量。每个测试都包含一个长度为L的字符串。

1 <= T <= 100

3 <= L <= 1000

A <= S [I] <= Z

该字符串包含至少三个不同的字符。


产量

对于每个测试用例，打印最长的字符串。案例1：两个最大长度的字符串是可能的 - “CBA”和“RPQ”。但他希望字符串具有更高的ASCII值，因此输出为“RPQ”。案例2：最大长度的字符串为“JGDA”。


样本输入1

2
ABCPQR
ADGJPRT
样本输出1

RQP
JGDA
'''
def down(s):
    s_list=[]
    for char in s:
        s_list.append(ord(char))
    # print(s_list)
    # print(type(s_list[0]))#十进制int
    s_list.sort(reverse=True)
    print(s_list)






if __name__ == '__main__':
    count=int(input())
    for i in range(count):
        down(input())