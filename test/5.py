if __name__ == '__main__':
    length=int(input())
    for index in range(0,length):
        result=0
        str=input().split()
        if len(str)>=1:
            for index in range(1,len(str)):
                result = result+int(str[index])
            print(result)
        else:
            continue


        # if len(str)==1 and int(str[0]) == 0:
        #     break
        # el