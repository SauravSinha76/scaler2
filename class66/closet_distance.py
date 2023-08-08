import functools

def compare(x,y):
    dist_x = x[0] * x[0] + x[1] * x[1]
    dist_y = y[0] * y[0] + y[1] * y[1]

    return dist_y - dist_x
def solve(A,B):
    A.sort(key = functools.cmp_to_key(compare))
    return A[:B]



A = [
       [1, 3],
       [-2, 2]
     ]
B = 1
print(solve(A,B))