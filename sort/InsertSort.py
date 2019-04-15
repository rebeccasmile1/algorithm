def InsertSort(a):
    length=len(a)
    for i in range(1,length):
        if a[i]<a[i-1]:
            j=i-1
            x=a[i]
            while x<a[j] and j>=0:
                a[j+1]=a[j]
                j -= 1

            a[j+1]=x

if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    InsertSort(a)
    print(a)