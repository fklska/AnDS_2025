# E-Сортировка вагонов

import sys

def main():
    n = int(input())
    vagons = list(map(int, input().split()))
    need_vagon = 1
    put_count = 0
    out_count = 0
    stack = []
    operations_count = 0
    result = []
    for i in range(n):
        if vagons[i] != need_vagon:
            if len(stack) == 0:
                stack.append((vagons[i], vagons[i]))
            else:
                if vagons[i] > stack[-1][0]:
                    return 0

                stack.append((vagons[i], max(vagons[i], stack[-1][1])))
            put_count += 1

        else:
            result.append(f"1 {put_count + 1}")
            put_count = 0

            node = vagons[i]
            need_vagon += 1
            while stack and abs(node - stack[-1][0]) == 1:
                out_count += 1
                node = stack.pop()[0]
                need_vagon += 1

            operations_count += 2
            result.append(f"2 {out_count + 1}")
            out_count = 0

    if len(stack) != 0:
        return 0

    return f"{operations_count}\n" + "\n".join(result)


if __name__ == "__main__":
    print(main())