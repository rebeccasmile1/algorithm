def coin():
    money,n = list(map(int, input().strip().split()))
    coin_type=[]
    for i in range(n):
        coin_type.append(int(input()))
    count = 0
    c = len(coin_type) - 1
    while money:
        count+=money//(coin_type[c])
        money=money%coin_type[c]
        c -= 1
        if c==0 and money%coin_type[c]!=0:
            count=-1
            break
    return count;

print(coin())