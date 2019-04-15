'''
j从后面开始
每次把最小的冒泡到i位置
'''
def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
def BubbleSort2(a):
    for i in range(len(a)):
        j=len(a)-1
        while j>i:
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
            j-=1
if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    BubbleSort2(a)
    print(a)