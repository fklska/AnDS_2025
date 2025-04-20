import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    matrix = {}
    for i in range(1, n + 1):
        matrix[i] = []

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().strip().split())
        matrix[i].append(j)

    visited = [0] * (n + 1)  # 0 - белый 1 - серый 2 - черный

    for node in range(1, n + 1):
        if visited[node] != 2:
            if dfs(node, visited, matrix) == 1:
                return 1

    return 0


def dfs(node, visited, graph):
    visited[node] = 1

    for child in graph[node]:
        if visited[child] == 1:
            return 1

        if visited[child] != 2:
            if dfs(child, visited, graph) == 1:
                return 1

    visited[node] = 2

    return 0


if __name__ == "__main__":
    print(main())