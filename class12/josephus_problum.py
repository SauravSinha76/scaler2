def solve(A):
    killed =0
    s = 1
    while s <= A:
        killed = s
        s *=2
    return ((A -killed) * 2) +1

print(solve(100))