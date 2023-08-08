import heapq


def solve(A,B):
    n = len(A)
    heap =[]

    for i in range(n):
        for j in range(i+1, n):
            frac = - (A[i]/A[j])
            if len(heap) == B:
                heapq.heappush(heap, (frac,A[i],A[j]))
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,(frac,A[i],A[j]))
    ans = heapq.heappop(heap)
    return [ans[1],ans[2]]

def solve1(A,B):
    heap = []
    for a in A:
        if len(heap) < B:
            heapq.heappush(heap,-a)
        else:
            heapq.heappush(heap,-a)
            heapq.heappop(heap)
    return -heap[0]

A = [1, 2, 3, 5]
B = 3
print(solve1(A,B))