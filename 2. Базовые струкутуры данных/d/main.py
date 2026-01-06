# D-Шарики

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    stack = [(colors[0], 1)]
    res = 0
    for i in range(1, n):
        if stack[-1][0] != colors[i]:
            if stack[-1][1] >= 3:
                for _ in range(stack[-1][1]):
                    stack.pop()
                    res += 1

            stack.append((colors[i], 1 if colors[i] != stack[-1][0] else stack[-1][1] + 1))
        else:
            stack.append((colors[i], stack[-1][1] + 1))

    if stack[-1][1] >= 3:
        for _ in range(stack[-1][1]):
            stack.pop()
            res += 1

    return res


if __name__ == "__main__":
    print(main())