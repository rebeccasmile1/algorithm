def Swap2Balance(a,b,len):
    suma=sum(a)
    sumb=sum(b)
    diff=suma-sumb
    while diff!=0:
        besti=0
        bestj=0
        bestChange=0
        for i in range(0,len):
            for j in range(0,len):
                change=a[i]-b[j]
                if abs(diff-2*change)<abs(diff-2*bestChange):
                    besti=i
                    bestj=j
                    bestChange=change
        if bestChange==0:#差不能再缩小了
            return diff
        (a[besti],b[bestj])=(b[bestj],a[besti])
        suma=suma-bestChange
        sumb=sumb+bestChange
        diff=suma-sumb
    return  diff





if __name__ == '__main__':
    tempa=input().split()
    tempb=input().split()
    a=[]
    b=[]
    for e in tempa:
        a.append(int(e))
    for e in tempb:
        b.append(int(e))
    res=Swap2Balance(a,b,len(a))
    print(a,b)
    print(abs(sum(a)-sum(b)))


