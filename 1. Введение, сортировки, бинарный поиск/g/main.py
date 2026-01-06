# G-Anti-qsort test
import math


def main():
    n = int(input())
    result = list(range(1, n+1))
    for i in range(len(result)):
        result[i], result[i//2] = result[i//2], result[i]

    return result


if __name__ == "__main__":
    print(*main())