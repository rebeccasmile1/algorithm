def search(a, l, r):
    while (l < r):
        mid = l + (r - l) / 2.0
        ans = 0.0
        for i in range(len(a)):
            ans += 1.0 / (mid - a[i])
        if (abs(ans) < 1e-7):
            return mid
        if (ans > 0):
            l = mid
        else:
            r = mid
    return l

num = int(input())
for test_case in range(num):
    n = int(input())
    arr = list(map(int, input().split()))
    result=[]
    for i in range(n-1):
        result.append(search(arr,arr[i],arr[i+1]))
    print(" ".join(format(x,'.2f') for x in result))