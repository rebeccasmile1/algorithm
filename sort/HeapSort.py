'''
以大顶堆为例，这样排出来list里面正好是升序的
'''
def HeapSort(a):
    BuildingHeap(a)
    i=len(a)-1
    while i>0:#最后那一个不用排了
        a[i],a[0]=a[0],a[i]
        HeapAdjust(a,0,i)
        i-=1
    print(a)

def BuildingHeap(a):
    length=len(a)
    if length%2==1:
        i=(length-1)//2-1
    else:
        i = (length - 1) // 2  # 从最后一课子树开始,往上走
    while i>=0:#向上走
        HeapAdjust(a,i,length)
        i-=1
def HeapAdjust(a,s,length):#向下调整
    temp=a[s]#当前的根
    child=2*s+1#左孩子
    while child<length:
        if child+1<length and a[child]<a[child+1]:
            child+=1
        if a[s]<a[child]:
            a[s]=a[child]
            s=child
            child=2*child+1
        else:#因为每一步的下面都是好的，如果当前是满足的，则下面也是满足的
            break
        a[s]=temp





    pass
if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    HeapSort(a)
