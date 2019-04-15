'''
2
5
31 100 65 12 18
10 13 47 157 6
100 113 174 11 33
88 124 41 20 140
99 32 111 41 20
2
42 93 7 14

'''
if __name__ == '__main__':
    test_case = int(input())
    for i in range(0,test_case):
        n = int(input())
        matrix_info = list(map(int, input().strip().split(' ')))
        index = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                matrix[i][j] = matrix_info[index]
                index += 1
        visted = [[0 for i in range(n)] for j in range(n)]
        i,j,count = 0, 0, 0
        while True:
            if i == n-1 and j==n-2:#左边
                count += matrix[i][j] + matrix[n-1][n-1]
                break
            if i== n-2 and j== n-1:#上面
                count+= matrix[i][j] + matrix[n-1][n-1]
                break
            count += matrix[i][j]
            visted[i][j] = 1
            up = 0
            down = 0
            left = 0
            right = 0
            if j-1>=0 and visted[i][j-1]==0:
                up = matrix[i][j-1]
            else:
                up = 10000
            if j+1 <= n-1 and visted[i][j+1] == 0:
                down = matrix[i][j+1]
            else:
                down = 10000
            if i+1 <= n-1 and visted[i+1][j] == 0:
                right = matrix[i+1][j]
            else:
                right = 10000
            if i-1 >=0 and visted[i-1][j] == 0:
                left = matrix[i-1][j]
            else:
                left = 10000
            min_road = min(up,down,left,right)
            if left == min_road:
                i -= 1
            elif right == min_road:
                i += 1
            elif up == min_road:
                j -= 1
            elif down == min_road:
                j += 1

        print(count)
