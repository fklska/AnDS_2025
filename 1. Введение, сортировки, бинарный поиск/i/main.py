# I-Что? Да! Пузырек
def main():
    n = int(input())
    p = list(map(int, input().split()))

    storage = {}
    max_index = n
    result = "1 "
    for i in range(n):
        if max_index == p[i]:
            max_index -= 1
            while True:
                value = storage.get(max_index, False)
                if value:
                    storage.pop(max_index)
                    max_index -= 1
                else:
                    break

            result += f"{len(storage) + 1} "
        else:
            storage[p[i]] = True
            result += f"{len(storage) + 1} "

    return result


if __name__ == "__main__":
    print(main())