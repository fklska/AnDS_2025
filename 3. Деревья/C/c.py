import sys

def main():
    n  = int(input())

    left = 1
    right = n + 1
    mid = (left + right) // 2

    while left < right - 1:
        mid = (left + right) // 2
        response = query(mid)
        if response == "<":
            right = mid

        if response == ">=":
            left = mid

    print(f"! {left}")


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


if __name__ == "__main__":
    main()