#贪婪行，动态规划试试
if __name__ == '__main__':
    n=int(input())
    res=1024-n
    count=[64,16,4,1]
    count_64=0
    count_16=0
    count_4=0
    count_1=0

    count_64+=res//64
    res =res % 64
    count_16+=res//16
    res=res%16
    count_4+=res//4
    res=res%4
    count_1=res
    print(count_64+count_16+count_4+count_1)

