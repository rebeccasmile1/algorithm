"""
Description
将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。

Input
输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。

Output
输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。

Sample Input 1

8 1 2 3 4 5 6 7 8 3
8 a b c d e f g h 4
Sample Output 1

3 2 1 6 5 4 7 8
d c b a h g f e
"""
import sys
def invert():
    for line in sys.stdin:
        temp_list=line.split()
        if not temp_list:
            break
        length=int(temp_list[0])
        K=int(temp_list[-1])
        data_list=[]
        for i in range(1,length+1):
            data_list.append(temp_list[i])
        i=0
        while (i+K)<=length:
            s=0
            for j in range(i,i+K//2):
                (data_list[j],data_list[i+K-1-s])=(data_list[i+K-1-s],data_list[j])
                s+=1
            i+=K
        string=''
        for e in data_list:
            string+=e
            string+=' '
        print(string.strip())



if __name__ == '__main__':
    #字符可以比较大小
    # if 'a'>'b':
    #     print('a')
    # else:
    #     print('b')
    invert()



