'''
动态规划，到每一步最小的值
'''
def solve():
    n=int(input())
    monsters=list(map(int,input().strip().split()))
    money=list(map(int,input().strip().split()))
    least=money[0]#当前需要花的钱
    temp=monsters[0]#当前最大武力值之和
    for i in range(1,n):
        if monsters[i]>temp:
            least+=money[i]
            temp+=monsters[i]
    print(least)
solve()