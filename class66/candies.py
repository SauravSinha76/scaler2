import heapq


def solve(A,B):
    heapq.heapify(A)
    total_candies = 0
    while A and A[0] <= B:
        x = heapq.heappop(A)
        half = x // 2
        total_candies += half
        if A:
            y = heapq.heappop(A)
            heapq.heappush(A,(y+ x - half))

    return total_candies

A = [3, 2, 3]
B = 4

A = [1, 2, 1]
B = 2
print(solve(A,B))



