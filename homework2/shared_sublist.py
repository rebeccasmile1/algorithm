"""
Description
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


Input
输入为两行，一行一个字符串

Output
输出如果有多个则分为多行，先后顺序不影响判断。

Sample Input 1

1A2BD3G4H56JK
23EFG4I5J6K7

Sample Output 1

23G456K
23G45JK
"""
def longest_sub():
    sA=input()
    sB=input()
    dict={}
    listA=list(sA)
    listB=list(sB)

    for i in listA:
        dict[i]=1
    for i in listB:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
    # print(dict)
    dict2={}
    for i in dict.keys():
        if dict[i]>1:
            dict2[i]=1
    # print(dict2)

    s1=''
    s2=''
    for i in listA:
        if i in dict2.keys():
            s1+=i

    for i in listB:
        if i in dict2.keys():
            s2+=i

    print(s1.strip())
    print(s2.strip())



if __name__ == '__main__':
    longest_sub()