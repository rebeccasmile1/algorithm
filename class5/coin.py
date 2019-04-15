'''
2
3 11
1 2 5
2 7
2 6

1
4 20
1 2 5 10

'''
def coin(coin_type,money):
    count=0
    c=len(coin_type)-1
    # for c in range(len(coin_type)-1,-1,-1):
    #     count+=money//(coin_type[c])
    #     money=money%(coin_type[c])
    #     if (c-1)==0 and money%coin_type[c-1]!=0:
    #         count=-1
    #         break
    # return count
    while money:
        count+=money//(coin_type[c])
        money=money%coin_type[c]
        c -= 1
        if c==0 and money%coin_type[c]!=0:
            count=-1
            break
    return count;


if __name__ == '__main__':
    cases=int(input())
    result=[]
    for i in range(cases):
        coin_types, money= list(map(int, input().strip().split()))
        # coin_types, money=temp_list[0],temp_list[1]
        coin_type=list(map(int,input().strip().split(' ')))
        result.append(coin(coin_type,money))
    for j in range(len(result)):
        print(result[j])





