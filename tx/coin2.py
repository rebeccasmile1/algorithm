import sys
def solve():
    m, n = sys.stdin.readline().strip().split()
    m, n = int(m), int(n)
    coins = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        coins.append(int(line.strip()))
    matrix = [[[]] * (m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(1, 1 + m):
            if i == 0:
                matrix[i][j] = [coins[i]] * (j // coins[i]) if j % coins[i] == 0 else -1
            else:
                k = j // coins[i]
                for t in range(k, -1, -1):
                    if not matrix[i - 1][j - k * coins[i]] == [-1]:
                        matrix[i][j] = k * [coins[i]] + matrix[i - 1][j - k * coins[i]]
                        break
                    if not matrix[i][j]:
                        matrix[i][j] = [-1]
    result_map = {}
    for c in coins:
        result_map[c] = 0
    for t in matrix[-1]:
        if t == [-1]:
            return -1
        if sum([k * v for k, v in result_map.items()]) >= sum(t):
            continue
        for c in coins:
            if t.count(c) > result_map[c]:
                result_map[c] = t.count(c)
    print(sum(result_map.values()))
solve()