def question2():
    def isin(pi, pj, pk, p0):
        x1 = float(p0[0])
        x2 = float(pj[0])
        x3 = float(pi[0])
        x4 = float(pk[0])
        y1 = float(p0[1])
        y2 = float(pj[1])
        y3 = float(pi[1])
        y4 = float(pk[1])

        k_j0 = 0
        b_j0 = 0
        k_k0 = 0
        b_k0 = 0
        k_jk = 0
        b_jk = 0
        perpendicular1 = False
        perpendicular2 = False
        perpendicular3 = False
        # pj,p0组成的直线，看pi,pk是否位于直线同一侧

        if x2 - x1 == 0:
            # pj,p0组成直线垂直于X轴时
            t1 = (x3 - x2) * (x4 - x2)
            perpendicular1 = True
        else:
            k_j0 = (y2 - y1) / (x2 - x1)
            b_j0 = y1 - k_j0 * x1
            t1 = (k_j0 * x3 - y3 + b_j0) * (k_j0 * x4 - y4 + b_j0)

        # pk,p0组成的直线，看pi,pj是否位于直线同一侧

        if x4 - x1 == 0:
            # pk,p0组成直线垂直于X轴时
            t2 = (x3 - x1) * (x2 - x1)
            perpendicular2 = True
        else:
            k_k0 = (y4 - y1) / (x4 - x1)
            b_k0 = y1 - k_k0 * x1
            t2 = (k_k0 * x3 - y3 + b_k0) * (k_k0 * x2 - y2 + b_k0)

        # pj,pk组成的直线，看pi,p0是否位于直线同一侧

        if x4 - x2 == 0:
            # pj,pk组成直线垂直于X轴时
            t3 = (x3 - x2) * (x1 - x2)
            perpendicular3 = True
        else:
            k_jk = (y4 - y2) / (x4 - x2)
            b_jk = y2 - k_jk * x2
            t3 = (k_jk * x3 - y3 + b_jk) * (k_jk * x1 - y1 + b_jk)
        # 如果pk，p0,pj，三点位于同一直线时，不能将点删除
        if (k_j0 * x4 - y4 + b_j0) == 0 and (k_k0 * x2 - y2 + b_k0) == 0 and (k_jk * x1 - y1 + b_jk) == 0:
            t1 = -1
        # 如果pk，p0,pj，三点位于同一直线时且垂直于X轴，不能将点删除
        if perpendicular1 and perpendicular2 and perpendicular3:
            t1 = -1

        return t1, t2, t3

    def force(lis, n):
        # 集合S中点个数为3时，集合本身即为凸包集
        if n == 3:
            return lis
        else:
            # 集合按纵坐标排序，找出y最小的点p0
            lis.sort(key=lambda x: x[1])
            p0 = lis[0]
            # 除去p0的其余点集合lis_brute
            lis_brute = lis[1:]
            # temp是用来存放集合需要删除的点在lis_brute内的索引，四个点中如果有一个点在其余三个点组成的三角形内部，则该点一定不是凸包上的点
            temp = []
            # 三重循环找到所有这样在三角形内的点
            for i in range(len(lis_brute) - 2):
                pi = lis_brute[i]
                # 如果索引i已经在temp中，即pi一定不是凸包上的点，跳过这次循环
                if i in temp:
                    continue
                for j in range(i + 1, len(lis_brute) - 1):
                    pj = lis_brute[j]
                    # 如果索引j已经在temp中，即pj一定不是凸包上的点，跳过这次循环
                    if j in temp:
                        continue
                    for k in range(j + 1, len(lis_brute)):
                        pk = lis_brute[k]

                        # 如果索引k已经在temp中，即pk一定不是凸包上的点，跳过这次循环
                        if k in temp:
                            continue
                        # 判断pi是否在pj,pk,p0构成的三角形内
                        (it1, it2, it3) = isin(pi, pj, pk, p0)
                        if it1 >= 0 and it2 >= 0 and it3 >= 0:
                            if i not in temp:
                                temp.append(i)
                        # 判断pj是否在pi,pk,p0构成的三角形内
                        (jt1, jt2, jt3) = isin(pj, pi, pk, p0)
                        if jt1 >= 0 and jt2 >= 0 and jt3 >= 0:

                            if j not in temp:
                                temp.append(j)

                        # 判断pk是否在pj,pi,p0构成的三角形内
                        (kt1, kt2, kt3) = isin(pk, pi, pj, p0)
                        if kt1 >= 0 and kt2 >= 0 and kt3 >= 0:

                            if k not in temp:
                                temp.append(k)
            # listlast是最终选出的凸包集合
            lislast = []
            for coor in lis_brute:
                loc = [i for i, x in enumerate(lis_brute) if x == coor]
                for x in loc:
                    ploc = x
                if ploc not in temp:
                    lislast.append(coor)
            # 将p0加入凸包集合
            lislast.append(p0)
            return lislast

    total = int(input().strip())

    while 1:
        try:
            num = int(input().strip())
            if num <= 2:
                print(-1)
                input()
                continue
            arr = []
            line = list(map(int, input().strip().split()))
            for j in range(num):
                arr.append((line[j * 2], line[2 * j + 1]))
            res = force(arr, len(arr))
            res.sort(key=lambda x: x[0])
            ans = ''
            for j in range(len(res)):
                ans += str(res[j][0]) + ' ' + str(res[j][1]) + ', '
            print(ans.strip()[:-1])
        except Exception as e:
            break