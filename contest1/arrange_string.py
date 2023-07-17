def solve(A):
    A.sort(key=len)
    return A

A =[ "hi", "he", "hello"]
A = ["bat","cat","but", "could"]
print(solve(A))