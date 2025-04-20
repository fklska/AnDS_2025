import sys
from collections import deque

def main():
    m = int(sys.stdin.readline().strip())

    graph = {}

    for _ in range(m):
        el1, el2 = sys.stdin.readline().strip().split(" -> ")
        if el1 in graph:
            graph[el1].append(el2)
        else:
            graph[el1] = [el2]

    depth = 0

    have = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()

    q = deque([(have, depth)])

    visited = set()

    while q:
        node, depth = q.popleft()
        if node in visited:
            continue

        visited.add(node)

        if node == target:
            return depth

        if node in graph:
            for child in graph[node]:
                q.append((child, depth + 1))

    return -1


if __name__ == "__main__":
    print(main())