def SelectionSort(a):
    length=len(a)
    for i in range(length):
        min=i
        for j in range(i,length):
            if a[j]<a[min]:
                min=j
        a[min],a[i]=a[i],a[min]
def SelectionSort2(a):
    length=len(a)
    for i in range(length//2):
        min=i
        max=i
        for j in range(i+1,length-i):
            if a[max]<a[j]:
                max=j
                continue
            if a[min]>a[j]:
                min=j
        print(a[max],a[min])

        #注意，此方法可能会有bug,就是当如1,4,6，交换位置里存放的是最大或者最小值，则交换的时候会受影响，还是要用方法一更稳妥

        (a[max], a[length - 1 - i]) = (a[length - 1 - i], a[max])
        (a[min], a[i]) = (a[i], a[min])
        # if max!=length-1-i:
        #     a[max], a[length - 1 - i] = a[length - 1 - i], a[max]
        # elif max==i:
        #
        # if min!=i:
        #     a[min], a[i] = a[i], a[min]



if __name__ == '__main__':
    a=[38,49,65,97,76,13,27,49]
    SelectionSort(a)
    print(a)