# 문제1
def stairs_count(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    table = [None] * (n + 1)
    table[0] = 1
    if n >= 1:
        table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

if __name__ == "__main__":
    n = int(input("계단의 개수를 입력하시오: ").strip())
    num = stairs_count(n)
    print(f"{n}개의 계단을 오르는 방법의 수는 {num}가지입니다.")
