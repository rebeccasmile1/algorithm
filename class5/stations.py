'''
Description

Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.

Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival and departure times must not be same for a train.


Input

The first line of input contains T, the number of test cases. For each test case, first line will contain an integer N, the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.

Note: Time intervals are in the 24-hourformat(hhmm), preceding zeros are insignificant. 200 means 2:00.
Consider the example for better understanding of input.

Constraints:1 <= T <= 100，1 <= N <= 1000，1 <= A[i] < D[i] <= 2359


Output

For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.


Sample Input 1


1
6
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000

3
'''
def stations(train_number,arrival_time,depart_time):
    a_index=1
    d_index=0
    platforms=0
    for i in range(train_number-1):
        if depart_time[i]>arrival_time[i+1]:
            platforms+=1
    return platforms
if __name__ == '__main__':
    cases=int(input())
    result=[]
    for i in range(cases):
        train_number=int(input())
        arrival_time=list(map(int,input().strip().split()))
        depart_time=list(map(int,input().strip().split()))
        result.append(stations(train_number,arrival_time,depart_time))
    for j in range(len(result)):
        print(result[j])