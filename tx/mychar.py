'''
4
1100
'''
def solve():
    length=int(input())
    str_list=input()
    # print(length,str,type(str))
    if length!=len(str_list):
        return
    data=[]
    for i in str_list:
        if i=='0':
            data.append(0)
        else:
            data.append(1)

    temp=data
    flag=False
    while data:
        for i in range(1,len(data)):
            if data[i-1]^data[i]==1:
                data[i-1]=9
                data[i]=9
            temp_str=[]
            # print(str)
            for j in range(len(data)):
                if data[j]!=9:
                    temp_str.append(data[i])
            data=temp_str
            # print(str)
            if temp==data:
                flag=True
                break
        if flag==True:
            break
    return len(data)

print(solve())