"""
Description
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


Input
输入为两行，一行一个字符串

Output
输出如果有多个则分为多行，先后顺序不影响判断。

Sample Input 1

1A2BD3G4H56JK
23EFG4I5J6K7

Sample Output 1

23G456K
23G45JK
"""


class LCS():
    def input(self, x, y):
        # 读入待匹配的两个字符串
        if type(x) != str or type(y) != str:
            print
            'input error'
            return None
        self.x = x
        self.y = y

    def Compute_LCS(self):
        xlength = len(self.x)
        ylength = len(self.y)
        self.direction_list = [None] * xlength  # 这个二维列表存着回溯方向
        # print(self.direction_list)
        for i in range(xlength):
            self.direction_list[i] = [None] * ylength
        # print(self.direction_list)
        self.lcslength_list = [None] * (xlength + 1)
        # print(len(self.lcslength_list))
        # 这个二维列表存着当前最长公共子序列长度，0列全为0，0行全为0
        for j in range(xlength + 1):
            self.lcslength_list[j] = [None] * (ylength + 1)
        for i in range(0, xlength + 1):
            self.lcslength_list[i][0] = 0
        for j in range(0, ylength + 1):
            self.lcslength_list[0][j] = 0
        # 下面是进行回溯方向和长度表的赋值
        for i in range(1, xlength + 1):
            for j in range(1, ylength + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j - 1] + 1
                    self.direction_list[i - 1][j - 1] = 0  # 左上
                elif self.lcslength_list[i - 1][j] > self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 1  # 上
                elif self.lcslength_list[i - 1][j] < self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i][j - 1]
                    self.direction_list[i - 1][j - 1] = -1  # 左
                else:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 2  # 左或上
        self.lcslength = self.lcslength_list[-1][-1]
        return self.direction_list, self.lcslength_list

    def printLCS(self, curlen, i, j, s):
        if i == 0 or j == 0:
            return None

        if self.direction_list[i - 1][j - 1] == 0:
            if curlen == self.lcslength:
                s += self.x[i - 1]
                for i in range(len(s) - 1, -1, -1):
                    print(s[i], end='')
                print('\n')

            elif curlen < self.lcslength:
                s += self.x[i - 1]
                self.printLCS(curlen + 1, i - 1, j - 1, s)
        elif self.direction_list[i - 1][j - 1] == 1:
            self.printLCS(curlen, i - 1, j, s)
        elif self.direction_list[i - 1][j - 1] == -1:
            self.printLCS(curlen, i, j - 1, s)
        else:
            self.printLCS(curlen, i - 1, j, s)
            self.printLCS(curlen, i, j - 1, s)

    def returnLCS(self):
        # 回溯的入口
        self.printLCS(1, len(self.x), len(self.y), '')


if __name__ == '__main__':
    p = LCS()
    listA = input()
    listB = input()
    p.input(listA, listB)
    p.Compute_LCS()
    p.returnLCS()
