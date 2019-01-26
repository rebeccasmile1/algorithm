'''
福康方法
    # 本题应将书进行二分查找，
    # 二分法的起始位置应选取start = max(pages)以保证一人一本的页数最大的最小是max，
    # 结束位置为一个人抄完所有书，即total = sum(pages)，一个人分到所有的
    # 判断条件是是否超过规定人数，
    # 如果超过则增大任务量，
    # 否则减少任务量，从而逐渐缩小任务量范围。
'''
def distribute(pages,k):
    if pages==None or len(pages)==0 :
        return 0
    total=0
    maxp=pages[0]
    for i in range(len(pages)):
        total+=pages[i]
        if maxp<pages[i]:
            maxp=pages[i]
    start=maxp
    end=total
    while start+1<end:
        mid=start+(end-start)//2
        if countCopiers(pages,mid)>k:#如果人数太多了，选大页码分配，将start右移
            start=mid
        else:#人数不够或者正好，那么分配小页码，将end左移
            end=mid
    if countCopiers(pages,start)<=k:#如果较小的页码就能满足人数要求，则返回小的页码，否则小页码需求的人太多，返回较大的页码
        return start
    else:
        return end
def countCopiers(pages,limit):#计算每个人分Limit页码时候，至少需要几个人
    if pages==None or len(pages)==0:
        return -1
    copiers =1
    sum=0
    for i in range(len(pages)):
        if sum+pages[i]>limit:#如果超过页码，则增加人，清空sum
            copiers+=1
            sum=0
        sum+=pages[i]#将当前的书加入sum，如果刚刚超过工作量，则这是下一个人的书，否则就继续加这本书
    return copiers
T=int(input())
for i in range(T):
    p=int(input())
    pages=[]
    str1=input().split()
    for i in range(p):
        pages.append(int(str1[i]))
    m=int(input())
    k=distribute(pages,m)
    print(k)