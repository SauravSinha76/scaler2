def solve(A):
    unique = set()
    psum = 0
    unique.add(psum)
    for a in A:
        psum += a
        unique.add(psum)

    if len(unique) == len(A) + 1:
        return 0
    else:
        return 1

A = [1, 2, 3, 4, 5]
A = [4, -1, 1]
print(solve(A))