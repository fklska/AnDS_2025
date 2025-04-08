def main():
    n, k = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    arr_k = list(map(int, input().split()))

    for i in range(k):
        print(bin_search(n, arr_k[i], seq))

def bin_search(n, k, arr):
    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return "YES"

        if arr[mid] > k:
            right = mid
        else:
            left = mid + 1

    return "NO"


if __name__ == "__main__":
    main()