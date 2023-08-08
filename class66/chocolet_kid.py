import heapq


def solve(A,B):
    B = [b * -1 for b in B]
    heapq.heapify(B)
    total_chocolet = 0
    while A > 0 and len(B) > 1:
        chocolet = heapq.heappop(B)
        heapq.heappush(B,-(-chocolet // 2))
        total_chocolet -= chocolet
        A -= 1
    return total_chocolet

A = 3
B = [6, 5]
A = 5
B = [2, 4, 6, 8, 10]
print(solve(A,B))
