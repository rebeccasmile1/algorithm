'''
2
2
1 2
4
1 2 3 3
'''

def giveRewardsCore(rewards,scores,l,m,r):

    left=scores[l]
    mid=scores[m]
    right=scores[r]
    max_rewards =left
    min_rewards=left
    if left>right :
        max_rewards=left
        min_rewards=right
    else:
        max_rewards=right
        min_rewards=left
    minus=max_rewards-mid

    if rewards[m]>max_rewards:
        return minus
    elif rewards[m]<min_rewards:
        return 0
    else:
        return minus

def giveRewards(n,scores):
    rewards = [1 for i in range(n)]

    for i in range(0,n):
        if i==0:
            rewards[i]+=giveRewardsCore(rewards,scores,len(scores)-1,0,1)
        elif i==len(scores)-1:
            rewards[i]+=giveRewardsCore(rewards,scores,len(scores)-2,len(scores)-1,0)
        else:
            rewards[i]+=giveRewardsCore(rewards,scores,i-1,i,i+1)
    print(rewards)

if __name__ == '__main__':
    cases=int(input())
    # data=[]
    for i in range(cases):
        n=int(input())
        scores=list(map(int,input().strip().split()))
        giveRewards(n,scores)