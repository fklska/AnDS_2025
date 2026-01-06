# H-Зеркальный код

def main():
    n = int(input())
    line = input()
    letters = []
    for i in set(line):
        letters.append((i, line.count(i)))


    left = ""
    right = ""
    mid = ""
    letters = sorted(letters, key=lambda x: x[0])
    first_odd = False

    for item in letters:
        if item[1] % 2 == 1:
            if not first_odd:
                mid = item[0]
                first_odd = True

            left = left + item[0] * ((item[1] - 1) // 2)
            right = item[0] * ((item[1] - 1) // 2) + right
        else:
            left = left + item[0] * (item[1] // 2)
            right = item[0] * (item[1] // 2) + right

    return left + mid + right


if __name__ == "__main__":
    print(main())