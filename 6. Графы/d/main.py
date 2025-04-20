import sys
from collections import deque

def main():

    n = int(sys.stdin.readline().strip())
    x1, y1 = map(int, sys.stdin.readline().strip().split())
    x2, y2 = map(int, sys.stdin.readline().strip().split())

    q = deque([(x1, y1)]) # (x, y, [(path)]))

    moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
    parent = {}
    parent[(x1, y1)] = None

    while len(q) > 0:
        u = q.popleft()

        if u == (x2, y2):
            coords = u
            path = [coords]
            while parent[coords] is not None:
                coords = parent[coords]
                path.append(coords)

            path.reverse()
            return path

        for dx, dy in moves:
            nx = u[0] + dx
            ny = u[1] + dy
            if (nx, ny) not in parent:
                if (nx > 0 and nx <= n) and (ny > 0 and ny <= n):
                    parent[(nx, ny)] = u
                    q.append((nx, ny))


if __name__ == "__main__":
    result = main()
    print(len(result) - 1)
    for point in result:
        print(*point)
