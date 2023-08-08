import heapq


def solve(A):
    ans =[-1,-1]
    if len(A) < 3:
        return ans
    p = A[0] * A[1] * A[2]
    ans.append(p)
    heap = [A[0],A[1],A[2]]
    heapq.heapify(heap)
    for i in range(3, len(A)):
        if heap[0] < A[i]:
            p *= A[i]
            val = heapq.heappop(heap)
            p //= val
            ans.append(p)
            heapq.heappush(heap,A[i])
    return ans
A = [1, 2, 3, 4, 5]
A = [10, 2, 13, 4]
print(solve(A))