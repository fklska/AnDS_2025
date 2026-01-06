# A-Минимум на стеке
class MinStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        if len(self.items) == 0:
            self.items.append((value, value))
        else:
            self.items.append((value, min(value, self.items[-1][1])))

    def pop(self):
        return self.items.pop()

    def min_seek(self):
        return self.items[-1][1]


def main():
    n = int(input())
    my_stack = MinStack()
    for _ in range(n):
        t = list(map(int, input().split()))
        if t[0] == 1:
            my_stack.push(t[1])
            continue
        if t[0] == 2:
            my_stack.pop()
            continue

        print(my_stack.min_seek())


if __name__ == "__main__":
    main()