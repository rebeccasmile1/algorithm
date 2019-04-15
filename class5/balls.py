'''
Description

There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road). The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help Geek to collect the maximum number of balls.


Input

The first line of input contains T denoting the number of test cases. The first line of each test case contains two integers N and M, denoting the number of buckets on road1 and road2 respectively. 2nd line of each test case contains N integers, number of balls in buckets on the first road. 3rd line of each test case contains M integers, number of balls in buckets on the second road.

Constraints:1<= T <= 1000，1<= N <= 10^3，1<= M <=10^3，0<= A[i],B[i]<=10^6


Output

For each test case output a single line containing the maximum possible balls that Geek can collect.


Sample Input 1

1
5 5
1 4 5 6 8
2 3 4 6 9
Sample Output 1

29
'''
def most_balls(A,B):
    count=0
    index=0
    temp_list=A
    flag=True
    while True:#和指针走的思想一样，这里用temp_list和flag配合
        if index==len(temp_list):
            break
        if B[index]!=A[index]:
            count+=temp_list[index]
            index+=1
        else:
            if (index<len(A)-1 and index<len(B)-1 and A[index+1]>B[index+1]+B[index]):
                count+=A[index]
                count+=A[index+1]
                index+=2
                continue
            else:
                if flag:#为True是从A指向B
                    temp_list=B
                    flag=False
                else:
                    temp_list=A
                    flag=True
                count+=temp_list[index]*2
                index+=1
    return count




if __name__ == '__main__':
    cases=int(input())
    result=[]
    for i in range(cases):
        N,M=list(map(int,input().strip().split()))
        N_balls=list(map(int,input().strip().split()))
        M_balls=list(map(int,input().strip().split()))
        if N_balls[0] > M_balls[0]:
            result.append(most_balls(N_balls,M_balls))
        else:
            result.append(most_balls(M_balls,N_balls))
    for j in range(cases):
        print(result[j])
