import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    matrix = {}
    for i in range(1, n + 1):
        matrix[i] = []

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().strip().split())
        matrix[i].append(j)
        matrix[j].append(i)

    visited = set()
    comps = []
    for node in range(1, n + 1):
        if node in visited:
            continue

        q = deque()
        q.append(node)
        visited.add(node)
        curr = []
        while len(q) > 0:
            u = q.popleft()
            curr.append(u)

            for i in matrix[u]:
                if i in visited:
                    continue

                q.append(i)
                visited.add(i)

        comps.append(sorted(curr))

    print(len(comps))
    for component in comps:
        print(len(component))
        print(*component)


if __name__ == "__main__":
    main()