'''
空间复杂度优秀的算法
只有前一个比后一个大，就往后交换
'''
def bubble(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    print(data)
data=[2,48,3,6,8,2,1]
bubble(data)