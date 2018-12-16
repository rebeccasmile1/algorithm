def hanoi(n,a,b,c):#先将所有的小的移动到c，再把最大的放到b，再把所有小的放到a,再把大的放到c，小的放到c，所以移动三次小的，两次大的
    if n==1:
        return 2
    else:
        return 3*hanoi(n-1,a,b,c)+2

if __name__ == '__main__':
    n=int(input())
    a=[]
    b=[]
    c=[]

    for index in range(0,n):
        a.append(index)
    print(hanoi(n, a, b, c))

    # print(count)
