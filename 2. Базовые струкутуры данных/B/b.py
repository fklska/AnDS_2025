# B-Минимум на отрезке
import sys
from collections import deque

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    deq = deque()
    result = []

    for i in range(n):
        if i >= k and i - k == deq[0]:
            deq.popleft()

        while deq and numbers[deq[-1]] > numbers[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(str(numbers[deq[0]]))

    return " ".join(result)


if __name__ == "__main__":
    print(main())