def parentheses(n, open, close, ans, s):
    if open == n and close == n:
        ans.append(s)
        return

    if open < n:
        parentheses(n, open + 1, close, ans, s + "(")
    if close < open:
        parentheses(n, open, close + 1, ans, s + ")")

def solve(n):
    ans =[]
    parentheses(n, 0, 0, ans, "")
    return ans

print(solve(3))