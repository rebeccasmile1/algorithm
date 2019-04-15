'''
20 4
1
2
5
10

5
'''
def coin():
    m,n = list(map(int, input().strip().split()))
    coin_type=[]
    for i in range(n):
        coin_type.append(int(input()))
    res = []
    flag=True
    for money in range(1,m+1):
        c = len(coin_type) - 1
        count = 0
        while money:
            count += money // (coin_type[c])
            money = money % coin_type[c]
            c -= 1
            if c == 0 and money % coin_type[c] != 0:
                count = -1
                flag=False
                break
        if flag==False:
            break
        res.append(count)
        print(count)
    max=0
    for c in res:
        if c>max:
            max=c

    return max;
print(coin())