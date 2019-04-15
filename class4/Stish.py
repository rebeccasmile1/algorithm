'''
背包问题，时间就是重量，只能少不能多，分数就是价值，够了就行
Description

Satish wants to prepare for tommorow's exam . He knows the distribution of marks for the subject along with time to learn the concepts.You are given remaining time for the exam along with marks for each topic and passing marks for the subject.Find the max marks Satish can attain by studing max no of topic in max no hours not excedding (p) .


Input

The first line of input contains the number of testcases t.The first line of each testcase contains the no of topics(n) , time remaining for exam(h) in hour and passing marks(p).Each 'n' lines contain u(time to learn topic) and v(weightage of topic in exam) .


Output

For each test case print "YES" along with time taken or "NO".

Constraints:

1<=t<=100

1<=n<=300

1<=h<=150

1<=p<=35

1<=u,v<=25


Sample Input 1

1
5 40 21
12 10
16 10
20 10
24 10
8 3
Sample Output 1

YES 36
'''
def distribution(content_info:list):
    time = content_info[1]
    marks = content_info[2]
    course_dict = {}
    course = []
    res = []
    for i in range(content_info[0]):
        tmp = list(map(int, input().strip().split(' ')))
        course_dict[tmp[0]]=tmp[1]#整理成为，重量：价值,因为重量都不同，但价值有同的
        course.append(tmp[0])
        course.sort()#按质量

    for i in range(content_info[0]):
        mark_count=0
        time_count=0
        time_count+=course[i]
        mark_count+=course_dict[course[i]]
        if time_count>time:#累计的，比阈值大
            time_count=0
            continue
        for j in range(i+1,content_info[0]):
            time_count+=course[j]
            if time_count<time:
                mark_count+=course_dict[course[j]]
            else:
                time_count-=course[j]
                break

        if mark_count>marks:
            res.append((time_count,mark_count))
    # print(res)
    if res:
        max=res[0][1]

        for i in res:
            if i[1]>max:
                max=i[1]
        for i in res:
            if i[1]==max:
                print('YES '+str(i[0]))
    else:
        print('NO')



if __name__ == '__main__':
    cases=int(input())
    for c in range(cases):
        content_info=list(map(int,input().strip().split(' ')))#依次是topics，remain time，marks
        distribution(content_info)



# import numpy as np
# def Stish(topics:int,passing_marks:int,remain_time:int):
#     listS=[]
#     for j in range(topics):
#         listu = input().split()
#         temp=[]
#         temp.append(int(listu[1]))
#         temp.append(int(listu[0]))
#         listS.append(temp)#价值，时间
#
#     # print(listS)
#     result=solve(listS,passing_marks,remain_time)
#     # print(result)
#
# def solve(listS:list,passing_marks:int,remain_time:int):
#     resArr=np.zeros((passing_marks+1,remain_time+1),dtype=np.int32)
#     for i in range(1,len()):
#         for j in range(1,remain_time+1):
#             if listS[i][1]<=j:
#                 resArr[i,j]=max(resArr[i-1,j-listS[i][1]+listS[i][0]],resArr[i-1,j])
#             else:
#                 resArr[i,j]=resArr[i-1,j]
#     return resArr[-1,-1]
#
#
#
# if __name__ == '__main__':
#     num=int(input())
#     for i in range(num):
#         temp_list=input().split()
#         topics=int(temp_list[0])
#         remain_time=int(temp_list[1])
#         passing_marks=int(temp_list[2])
#         print(topics,passing_marks,remain_time)
#         Stish(topics,passing_marks,remain_time)
