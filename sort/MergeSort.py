def MergeSort(a):
    if len(a)<=1:
        return a
    middle=len(a)//2
    left=MergeSort(a[:middle])
    right=MergeSort(a[middle:])
    return Merge(left,right)
def Merge(a,b):
    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    c+=a[i:]
    c+=b[j:]
    return c

def MergeSort2(a):#非递归，要解决的是小数组的商都怎么处理的问题
    i=1
    while i<len(a):#控制间隔
        low=0
        while low<len(a):#对于每个间隔，挨个做
            mid=low+i
            high=min(low+2*i,len(a))
            if mid<high:
                Merge2(a,low,mid,high)
            low+=2*i
        i*=2
def Merge2(a,low,mid,high):
    left=a[low:mid]
    right=a[mid:high]
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    a[low:high]=result

if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    result=MergeSort(a)
    print(result)
    b = [38, 49, 65, 97, 76, 13, 27, 49]
    MergeSort2(b)
    print(b)