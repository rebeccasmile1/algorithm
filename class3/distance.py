'''
描述

在给定的笛卡尔平面中，有N个点。我们需要找到点对的数量（A，B）

A点和B点不重合。
曼哈顿距离和欧几里德点之间的距离应相等。
注意：一对2点（A，B）被认为与2点对（B，A）相同。

曼哈顿距离= | x2-x1 | + | y2-y1 |

欧几里德距离=（（x2-x1）^ 2 +（y2-y1）^ 2）^ 0.5其中点是（x1，y1）和（x2，y2）。

约束：1 <= T <= 50,1 <= N <= 2 * 10 ^ 5,0 <=（| Xi |，| Yi |）<= 10 ^ 9


输入

第一行由T个测试用例组成。对于每个测试用例：第一行由N，点数组成。下一行包含N对包含两个整数Xi和Yi，即X坐标和一个Point的Y坐标


产量

按上面的要求打印对数。
'''
def distance(points):
    pairs_num=0
    edistamce=0
    mdistance=0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            mdistance=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
            edistamce=((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**(1/2)
            if mdistance==edistamce:
                pairs_num+=1
    print(pairs_num)


if __name__ == '__main__':
    count=int(input())
    for i in range(count):
        point_num=int(input())
        points=[]
        for j in range(point_num):
            temp_list = []
            point=[]
            temp_list=input().split()
            for p in temp_list:
                point.append(int(p))
            points.append(point)
            distance(points)



