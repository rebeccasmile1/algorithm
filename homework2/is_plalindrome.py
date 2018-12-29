"""
Description
判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。

Input
输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值

Output
是回文则输出true，不是则输出false，一行表示一个链表的结果。

Sample Input 1
3 1 2 1
4 1 2 2 1
3 3 5 3
6 a b c d c a

Sample Output 1
true
true
true
false
"""
import sys
def is_plalindrome():
    for line in sys.stdin:
        flag='true'
        temp_list=line.split()
        if not temp_list:
            break
        length=int(temp_list[0])
        data_list=[]
        for i in range(1,length+1):
            data_list.append(temp_list[i])
        for i in range(0,(length)//2):
            if data_list[i]!=data_list[length-1-i]:
                flag= 'false'

                break
        print(flag)


if __name__ == '__main__':
    is_plalindrome()
