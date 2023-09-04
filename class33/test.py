
def solution(image, radius):
    n = len(image)
    m = len(image[0])
    ans =[[0 for col in range(m)]
          for row  in range(n)]
    for i in range(n):
        for j in range(m):
            total = 0
            count = 0
            for k in range(1, radius + 1):
                if i + k < n:
                    total += image[i + k][j]
                    count += 1
                if i - k > -1:
                    total += image[i - k][j]
                    count += 1
                if j + k < m:
                    total += image[i][j + k]
                    count += 1
                if j - k > -1:
                    total += image[i][j - k]
                    count += 1
                if i - k > -1 and j + k < m:
                    total += image[i - k][j + k]
                    count += 1
                if i - k > -1 and j - k > -1:
                    total += image[i - k][j - k]
                    count += 1
                if i + k < n and j + k < m:
                    total += image[i + k][j + k]
                    count += 1
                if i + k < n and j - k > -1:
                    total += image[i + k][j - k]
                    count += 1
            print(f"i:{i} -> j:{j} -> total:{total} -> count : {count}")
            mean = total // count

            ans[i][j] = (image[i][j] + mean) // 2

    return ans

A=[
    [9,3],
    [6,0]
]
print(solution(A,1))

