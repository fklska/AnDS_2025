import sys
from collections import defaultdict
import heapq


def main():
    n, m  = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)

    for _ in range(m):
        c1, c2, cost = map(int, sys.stdin.readline().strip().split())
        graph[c1].append((c2, cost))
        graph[c2].append((c1, cost))

    min_max = (float('inf'), 1)
    for city in range(1, n + 1):
        d = {i: float('inf') for i in range(1, n+1)}
        d[city] = 0

        heap = [(0, city)]

        while heap:
            distance, vertex = heapq.heappop(heap)

            if distance > d[vertex]:
                continue

            for child in graph[vertex]:
                new_dist = distance + child[1]
                if d[child[0]] > new_dist:
                    d[child[0]] = new_dist

                    heapq.heappush(heap, (new_dist, child[0]))

        excentricite = max(d.values())
        if min_max[0] > excentricite:
            min_max = (excentricite, city)

    print(min_max[1])


if __name__ == "__main__":
    main()