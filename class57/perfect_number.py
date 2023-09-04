from collections import deque


def solve(A):
    queue = deque()
    queue.append("")
    count = 0

    while count <= A:
        x = queue.popleft()
        ele = x + '1'
        count += 1
        if count == A:
            return ele + ele[::-1]
        queue.append(ele)

        ele = x + '2'
        count += 1
        if count == A:
            return ele + ele[::-1]
        queue.append(ele)


print(solve(5))