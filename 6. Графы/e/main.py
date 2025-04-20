import sys
import heapq

def main():
    k = int(sys.stdin.readline().strip())

    heap = []
    for d in range(1, 10):
        remainder = d % k
        heapq.heappush(heap, (d, remainder))

    visited = set()

    while heap:
        current_sum, remainder = heapq.heappop(heap)
        #print(current_sum, remainder)

        if remainder == 0:
            return current_sum

        if remainder in visited:
            continue

        visited.add(remainder)

        for d in range(0, 10):
            new_remainder = (remainder * 10 + d) % k
            new_sum = current_sum + d
            heapq.heappush(heap, (new_sum, new_remainder))


if __name__ == "__main__":
    print(main())
