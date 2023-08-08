import heapq


def solve(A,B):
    heap =[]
    for a in A:
        for aa in a:
            if len(heap) < B:
                heapq.heappush(heap,-aa)
            else:
                heapq.heappush(heap,-aa)
                heapq.heappop(heap)

    return - heap[0]

A = [[5, 9, 11],
    [9, 11, 13],
    [10, 12, 15],
    [13, 14, 16],
    [16, 20, 21]]
B = 12

print(solve(A,B))