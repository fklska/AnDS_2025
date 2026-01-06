# C-Постфиксная запись
def main():
    n = input().split()
    stack = []
    for i in n:
        if i == "+":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(int(a2) + int(a1))
            continue

        if i == "-":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(int(a2) - int(a1))
            continue

        if i == "*":
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(int(a2) * int(a1))
            continue

        stack.append(i)

    return stack.pop()


if __name__ == "__main__":
    print(main())