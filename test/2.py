import sys
if __name__ == '__main__':
    print("begin")
    data_list=[]
    length=int(input())
    for index in range(0,length):
        str=input().split()
        if(len(str)>=2):
            result=int(str[0])+int(str[1])
            print(result)



    # for line in sys.stdin:
    #     result = 0
    #     temp_str=line.split()#用空字符串分割
    #     if(len(temp_str)>=2):
    #         result=int(temp_str[0])+int(temp_str[1])
    #         print(result)

