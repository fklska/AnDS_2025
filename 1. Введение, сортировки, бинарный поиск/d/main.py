# Квадратный корень и квадратный квадрат
import math

def main():
    r = math.sqrt(10**10)
    l = 0
    c = float(input())
    while l < r:
        mid = (r + l) / 2

        res = mid**2 + math.sqrt(mid + 1)

        if abs(res - c) < 0.000001:
            return mid

        if res > c:
            r = mid
        else:
            l = mid


if __name__ == "__main__":
    print(main())