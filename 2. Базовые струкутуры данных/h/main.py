# H-Хорошие дни
import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    prefix_sum = [0]*n
    stack = [] # value || index

    max_sum = 0
    for i in range(n):
        prefix_sum[i] = prefix_sum[i-1] + numbers[i]

        if not stack or numbers[i] > stack[-1][0]:
            stack.append((numbers[i], i))
        else:
            tmp_index = i
            while stack and stack[-1][0] >= numbers[i]:

                tmp_index = stack[-1][1]
                if i - stack[-1][1] == 0:
                    max_sum = max(max_sum, stack[-1][0] * stack[-1][0])
                else:
                    if stack[-1][1] == 0:
                        diaposone_prefix_sum = prefix_sum[i-1]
                    else:
                        diaposone_prefix_sum = prefix_sum[i-1] - prefix_sum[stack[-1][1] - 1]

                    max_sum = max(max_sum, diaposone_prefix_sum * stack[-1][0])

                stack.pop()

            stack.append((numbers[i], tmp_index))

    while stack:
        if n - 1 == stack[-1][1]:
            max_sum = max(max_sum, stack[-1][0] * stack[-1][0])
        else:
            if stack[-1][1] == 0:
                diaposone_prefix_sum = prefix_sum[n-1]
            else:
                diaposone_prefix_sum = prefix_sum[n-1] - prefix_sum[stack[-1][1] - 1]

            max_sum = max(max_sum, diaposone_prefix_sum * stack[-1][0])

        stack.pop()

    return max_sum


if __name__ == "__main__":
    print(main())