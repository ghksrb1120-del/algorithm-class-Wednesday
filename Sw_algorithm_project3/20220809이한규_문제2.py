# 문제2
def knapsack(W, wt, val, names):
    n = len(wt)
    A = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w - wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    res = []
    w = W
    for i in range(n, 0, -1):
        if A[i][w] != A[i-1][w]:
            res.append(names[i-1])
            w -= wt[i-1]

    res.reverse()
    return A[n][W], res

if __name__ == "__main__":
    #테스트
    names = ['노트북','카메라','책','옷','휴대용 충전기']
    wt =    [3, 1, 2, 2, 1]
    val =   [12,10,6,7,4]

    W = int(input("배낭 용량을 입력 하세요 : ").strip())
    max_val, items = knapsack(W, wt, val, names)
    print("최대 만족도:", max_val)
    print("선택된 물건:", items)
