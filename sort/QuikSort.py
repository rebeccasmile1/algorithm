def QuikSort(a):
    stack=[]
    stack.append(len(a)-1)
    stack.append(0)
    while stack:
        left = stack.pop()
        right = stack.pop()
        pivot = Partition(a, left, right)
        if left<pivot:
            stack.append(pivot-1)
            stack.append(left)
        if right>pivot:
            stack.append(right)
            stack.append(pivot+1)
def QuikSort2(a,left,right):#递归
    if left==right:
        return
    pivot=Partition(a,left,right)
    if(left<pivot):
        QuikSort2(a,left,pivot-1)
    if(right>pivot):
        QuikSort2(a,pivot+1,right)
def Partition(a,left,right):
    temp=a[left]
    while left< right:
        while a[right]>=temp and left<right:#取了等于号，使得我不用走完left+=1
            right-=1
        a[left]=a[right]
        while a[left]<=temp and left<right:#取了等于号，使得我不用走完right-=1
            left+=1
        a[right]=a[left]
    a[left]=temp
    return left

if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    QuikSort(a)
    print(a)
    QuikSort2(a,0,len(a)-1)
    print(a)