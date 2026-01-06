# G-Гоблины и очереди
from collections import deque
import sys

def main():
    n = int(sys.stdin.readline().strip())
    queue_start = deque()
    queue_end = deque()

    start_len = 0
    end_len = 0

    for _ in range(n):
        goblin = sys.stdin.readline().strip().split()

        if goblin[0] == "+":
            queue_end.append(goblin[1])
            end_len += 1

        if goblin[0] == "*":
            queue_start.append(goblin[1])
            start_len += 1

        if goblin[0] == "-":
            start_len -= 1
            print(queue_start.popleft())

        # Балансировка

        if start_len < end_len:
            start_len += 1
            end_len -= 1
            queue_start.append(queue_end.popleft())

        else:
            if start_len - end_len > 1:
                start_len -= 1
                end_len += 1
                queue_end.appendleft(queue_start.pop())


if __name__ == "__main__":
    main()