'''
描述

你有N本书。每本ith书都有Pi页数。你必须为M个学生分配书籍。可以有很多方法或排列方式。在每个排列中，M个学生中的一个将被分配最大页数。在所有这些排列中，任务是找到特定的排列，其中分配给学生的最大页数最小于所有其他排列中的页面，并打印该最小值。每本书都将分配给一名学生。每个学生必须至少分配一本书。


输入

第一行包含表示测试用例数量的“T”。然后是T测试用例的描述：每个案例都以一个正整数N开头，表示书籍数量。第二行包含N个空格分隔的正整数，表示每本书的页面。第三行包含另一个整数M，表示数字学生约束：1 <= T <= 70,1 <= N <= 50,1 <= A [i] <= 250,1 <= M <= 50，注意：如果无法进行有效分配，则返回-1 ，并且分配应该是连续的（参见解释以便更好地理解）


产量

对于每个测试用例，输出一行包含每个学生必须阅读的最小页数以用于相应的测试用例。
1
4
12 34 67 90
2

113

'''
def book():
    num=int(input())
    if num<1 or num>70:
        return
    for i in range(num):
        book_num=int(input())
        temp_list=input().split()
        pages_list=[]
        for e in temp_list:
            if int(e)<1 or int(e)>250:
                return
            pages_list.append(int(e))
        student_num=int(input())
        if book_num<1 or book_num>50 or book_num<student_num:
            return
        if student_num<1 or student_num>50:
            return
        result_temp=[]
        for j in range(len(pages_list)):
            for t in range(pages_list):
                result_temp.append(j)

if __name__ == '__main__':
    book()