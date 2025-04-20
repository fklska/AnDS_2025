import sys
from collections import defaultdict


def main():
    n, m  = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v  = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)


    order = map(int, sys.stdin.readline().strip().split())
    position_in_order = {node: idx for idx, node in enumerate(order)}

    for node in graph:
        for child in graph[node]:
            if position_in_order[node] > position_in_order[child]:
                return "NO"

    return "YES"


def dfs(graph, node, visited):

    for child in graph[node]:
        if child not in visited:
            return dfs(graph, child, visited)

    visited.add(node)
    return node


if __name__ == "__main__":
    print(main())