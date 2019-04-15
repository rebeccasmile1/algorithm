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
def Partition(a,left,right):
    temp=a[left]
    while left< right:
        while a[right]>=temp and left<right:
            right-=1
        a[left]=a[right]
        left+=1
        while a[left]<=temp and left<right:
            left+=1
        a[right]=a[left]
        right-=1
    return left
if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    QuikSort(a)
    print(a)