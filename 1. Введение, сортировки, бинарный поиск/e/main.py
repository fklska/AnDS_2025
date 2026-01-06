# E-Корень кубического уравнения
def main():
    a, b, c, d = map(int, input().split())
    r = 10**10
    l = -(10**10)

    dif = r - l

    while dif > 0.00000001:
        mid = (r + l) / 2

        res = function(a, b, c, d, mid)

        if res == 0:
            return mid

        if res*function(a, b, c, d, l) < 0:
            r = mid
        else:
            l = mid

        dif = r - l

    return (r + l) / 2


def function(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d


if __name__ == "__main__":
    print(main())