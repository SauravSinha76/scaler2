import functools

def solve(A):
    def factor(n):
        count = 0
        i = 1
        while i * i < n:
            if n % i == 0:
                if n // i == i:
                    count += 1
                else:
                    count += 2
            i += 1
        return count

    def compare(x, y):
        factor_x = factor(x)
        factor_y = factor(y)

        if factor_x < factor_y:
            return -1
        elif factor_x == factor_y and x < y:
            return -1

        return 1
    A.sort(key = functools.cmp_to_key(compare))
    return A

A = [6, 8, 9]
print(solve(A))