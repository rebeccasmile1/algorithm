t=[];
t=[0]*101
t[0]=1;
for num in range(1,101):
    for num2 in range(0,num):
        t[num]=t[num-1-num2]*t[num2]+t[num]
    print(t[num])