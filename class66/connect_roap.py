import heapq


def solve(A):
    heapq.heapify(A)
    sum = 0
    while len(A) > 1:
        x = heapq.heappop(A)
        y = heapq.heappop(A)
        sum += (x + y)
        heapq.heappush(A,(x + y))
    return sum

A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
print(solve(A))
