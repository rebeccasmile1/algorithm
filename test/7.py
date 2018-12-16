import sys
if __name__ == '__main__':
    # fstr=input().split()
    # if len(fstr) >= 1:
    #     result = int(fstr[0]) + int(fstr[1])
    #     print(result)
    for line in sys.stdin:

        str=line.split(' ')
        result=0

        if len(str)>=1:

            result=int(str[0])+int(str[1])
            print(result)
            print(end='\n')#Python3一定要end='\n'，否则会两个空行
            
#
# import sys
# if __name__ == '__main__':
#     i=0
#     for line in sys.stdin:
#         i=i+1
#         str=line.split(' ')
#         result=0
#         if i==1:
#             if len(str) >= 1:
#                 result = int(str[0]) + int(str[1])
#                 print(result)
#         elif len(str)>=1:
#             print('\n')
#             result=int(str[0])+int(str[1])
#             print(result)