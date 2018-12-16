import sys
if __name__ == '__main__':
    for line in sys.stdin:
        result=0
        str=line.split()
        if int(str[0])>=0:
             for index in range(1,len(str)):
                result = result+int(str[index])
             print(result)
        else:
             continue



