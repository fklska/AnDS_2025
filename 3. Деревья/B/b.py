def main():
    n, k = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    arr_k = list(map(int, input().split()))

    for i in range(k):
        print(bin_search(n, arr_k[i], seq))

def bin_search(n, k, arr):
    left = 0
    right = n - 1

    mid = (left + right) // 2

    while left < right:

        if arr[mid] == k:
            return arr[mid]

        if arr[mid] > k:
            right = mid
        else:
            left = mid + 1

        mid = (left + right) // 2

    if mid == 0:
        return arr[mid]

    if abs(arr[mid-1] - k) == abs(arr[mid] - k):
        return arr[mid-1]

    if abs(arr[mid-1] - k) < abs(arr[mid] - k):
        return arr[mid-1]

    return arr[mid]


if __name__ == "__main__":
    main()