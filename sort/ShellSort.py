def ShellSort(a):
    length=len(a)
    dk=length//2
    while dk>=1:#控制间距
        for i in range(dk,length):#对每次组进行简单插入排序的操作
            if a[i]<a[i-dk]:
                j=i-dk
                x=a[i]
                while x<a[j] and j>=0:
                    a[j+dk]=a[j]
                    j-=dk
                a[j+dk]=x
        dk=dk//2

if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    ShellSort(a)
    print(a)