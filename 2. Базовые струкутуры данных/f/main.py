# F-Астроград

import sys

def main():
    n = int(sys.stdin.readline().strip())
    queue = []
    index_arr = {
        #index : enter_value
    }

    enter = 0
    leave = 0

    for _ in range(n):
        event_type = sys.stdin.readline().strip().split()

        if event_type[0] == "1":
            index_arr[int(event_type[1])] = enter
            enter += 1
            queue.append(event_type[1])

        if event_type[0] == "2":
            leave += 1
            queue.pop(0)

        if event_type[0] == "3":
            enter -= 1
            queue.pop()

        if event_type[0] == "4":
            print(index_arr[int(event_type[1])] - leave)

        if event_type[0] == "5":
            print(queue[0])


if __name__ == "__main__":
    main()