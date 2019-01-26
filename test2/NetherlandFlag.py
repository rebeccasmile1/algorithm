'''
荷兰国旗问题
'''
def NetherlandFlag():
    pass
def partition(arr,L,R,num):
    less=L-1
    more=R+1
    cur=L
    while cur<more:
        if arr[cur]<num:
            less+=1
            (arr[cur],arr[less])=(arr[less],arr[cur])
            cur+=1
        elif arr[cur]>num:
            more-=1
            (arr[cur],arr[more])=(arr[more],arr[cur])
        else:
            cur+=1

    return arr

if __name__ == '__main__':
    # NetherlandFlag()
    arr=[5,5,5,2,7,3,8,9]
    print(partition(arr,0,len(arr)-1,5))