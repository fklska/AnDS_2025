# F-Сортировка слиянием с приколом
import math

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    res, count = merge_sort(arr, 0)
    print(count)
    return res

def merge_sort(arr, count):
    if len(arr) == 1:
        return arr, count

    left, count = merge_sort(arr[0: len(arr)//2], count)
    right, count = merge_sort(arr[len(arr)//2:], count)

    result = []

    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            count += len(left) - l
            r += 1
        else:
            result.append(left[l])
            l += 1

    if l < len(left):
        result += left[l:]
    if r < len(right):
        result += right[r:]

    return result, count


if __name__ == "__main__":
    print(*main())