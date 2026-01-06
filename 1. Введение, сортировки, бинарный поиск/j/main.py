# J-Разбиение таблицы
def main():
    t = int(input())
    for _ in range(t):     
        n, m = map(int, input().split())
        print(find(n, m))

def find(n, m):
    l = 1   
    r = m
    first_column = (2 + (n - 1) * m) * n / 2

    mid = (l + r) // 2
    optimal_v = (m, float("inf"))
    while l < r:
        sum_to_m = (first_column + first_column + (mid - 1)*n) * mid / 2
        sum_m_to = (first_column + (mid) * n + first_column + (m - 1)*n) * (m - mid) / 2
        delta = sum_m_to - sum_to_m

        if optimal_v[1] > abs(delta):
            optimal_v = (mid + 1, abs(delta))

        if delta == 0:
            return f"V {mid + 1}"

        if delta > 0:
            l = mid + 1
        else:
            r = mid

        mid = (l + r) // 2

    l = 1
    r = n
    mid = (l + r) // 2
    optimal_h = (n, float("inf"))

    while l < r:
        sum_to_m = (1 + mid*m) * mid*m / 2
        sum_m_to = (mid*m + 1 + m*n) * (m*n - (mid*m)) / 2
        delta = sum_m_to - sum_to_m

        if optimal_h[1] > abs(delta):
            optimal_h = (mid + 1, abs(delta))

        if delta == 0:
            return f"H {mid + 1}"

        if delta > 0:
            l = mid + 1
        else:
            r = mid

        mid = (l + r) // 2

    return f"V {optimal_v[0]}" if optimal_v[1] < optimal_h[1] else f"H {optimal_h[0]}"


if __name__ == "__main__":
    main()