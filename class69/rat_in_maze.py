import sys


def check(i,j,maze):
    n = len(maze)
    m = len(maze[0])
    if i == n-1 and j == m - 1:
        return True
    if i < 0 or i >= n or j < 0 or j >= m or maze[i][j] == 1 or maze[i][j] == 2:
        return False

    maze[i][j] = 2

    return check(i-1,j,maze) or check(i+1,j,maze) or check(i,j-1,maze) or check(i,j + 1,maze)

dx =[-1,0,1,0]
dy= [0,-1,0,1]

def better_check(i,j,maze):
    n = len(maze)
    m = len(maze[0])

    if i == n-1 and j == m- 1:
        return True

    maze[i][j] = 2

    for k in range(len(dx)):
        ni = i + dx[k]
        nj = j + dy[k]

        if -1 < ni < n and -1 < nj < m and maze[ni][nj] == 0:
            state = better_check(ni,nj,maze)
            if state:
                return True
    return False



def solve(A):
    sys.setrecursionlimit(10 ** 6)
    print(better_check(0,0,A))

A= [
    [0,0,0,1,0,0],
    [0,1,0,1,0,1],
    [0,1,0,0,1,0],
    [0,0,1,0,1,0],
    [1,1,1,0,0,0],
    [0,0,0,1,1,0]
]
solve(A)