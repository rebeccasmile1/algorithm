if __name__ == '__main__':
    length = int(input())
    for line in range(0,length):
        str = input().split(' ')
        result = 0
        if int(str[0]) >= 1:
            for index in range(1,len(str)):
                result = result+int(str[index])
            print(result)
            print(end='\n')  # Python3一定要end='\n'，否则会两个空行
        else:
            continue
