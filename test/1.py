import sys
if __name__ == '__main__':

    data_list=[]

    for line in sys.stdin:
        result = 0
        temp_str=line.split()#用空字符串分割
        if(len(temp_str)>=2):
            result=int(temp_str[0])+int(temp_str[1])
            print(result)
            # data_list.extend(result)

    # print(data_list)

