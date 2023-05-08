def solve(A):
    n = len(A)

    even_prefix = [A[0]]
    odd_prefix =[0]
    for i in range(1,n):
        if i % 2 == 0:
            even_prefix.append(even_prefix[i-1] + A[i])
            odd_prefix.append(odd_prefix[i-1])
        else:
            odd_prefix.append(odd_prefix[i-1] + A[i])
            even_prefix.append(even_prefix[i-1])

    count =0
    for i in range(n):
        sum_even = odd_prefix[n-1] - odd_prefix[i]
        if i != 0:
            sum_even += even_prefix[i-1]

        sum_odd = even_prefix[n-1] - even_prefix[i]

        if i != 0:
            sum_odd += odd_prefix[i-1]

        if sum_odd == sum_even:
            count += 1

    return count

A=[2, 1, 6, 4]
# A=[1, 1, 1]
print(solve(A))