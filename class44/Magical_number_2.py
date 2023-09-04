def solve(A,B,C):
    num = min(B,C)
    count =1
    while True:
        if count == A:
            return num
        num += 1
        if num % B == 0 or num % C == 0:
            count += 1


def gcd(A,B):
    if B == 0:
        return A
    return gcd(B, A % B)

def lcm(A,B):
    return (A*B) // gcd(A,B)

def count_pos(A,B,mid):
    return mid // A + mid // B - mid // lcm(A,B)



def solve_o(A,B,C):
    l = min(B,C)
    r = A *min(B,C)
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        pos = count_pos(B,C,mid)

        if pos >= A:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans



A = 1
B = 2
C = 3

A = 4
B = 2
C = 3
print(solve(A,B,C))
print(solve_o(A,B,C))