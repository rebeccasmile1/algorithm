# 帮帮Stish
# Description
#
# Satish wants to prepare for tommorow's exam . He knows the distribution of marks for the subject along with time to learn the concepts.You are given remaining time for the exam along with marks for each topic and passing marks for the subject.Find the max marks Satish can attain by studing max no of topic in max no hours not excedding (p) .
#
#
# Input
#
# The first line of input contains the number of testcases t.
# The first line of each testcase contains the no of topics(n) ,
#  time remaining for exam(h) in hour and
#  passing marks(p).
# Each 'n' lines contain
# u(time to learn topic) and
# v(weightage of topic in exam) .
#
#
# Output
#
# For each test case print "YES" along with time taken or "NO".
#
# Constraints:
#
# 1<=t<=100
#
# 1<=n<=300
#
# 1<=h<=150
#
# 1<=p<=35
#
#1<=u,v<=25

def distribution():
    test_cases = int(input())
    for i in range(0, test_cases):
        content_info = list(map(int, input().strip().split(' ')))
        time = content_info[1]
        mark = content_info[2]
        dict = {}
        course = []
        res = []
        for i in range(0,content_info[0]):
            tmp = list(map(int, input().strip().split(' ')))
            dict[tmp[0]] = tmp[1]#重量：价值
            course.append(tmp[0])
            course.sort()

        for i in range(0, content_info[0]):
            mark_count = 0
            time_count = 0
            time_count += course[i]
            mark_count += dict[course[i]]
            if time_count > time:
                time_count = 0
                continue
            for j in range(i+1,content_info[0]):
                time_count += course[j]
                if time_count < time:
                    mark_count += dict[course[j]]
                else:
                    time_count -= course[j]
                    break
            if mark_count > mark:
                res.append((time_count,mark_count))
        if res:
            max = res[0][1]

            for i in res:
                if i[1] > max:
                    max = i[1]
            for i in res:
                if i[1] == max:
                    print('YES '+ str(i[0]))
        else:
            print('NO')


if __name__ == '__main__':
    distribution()

