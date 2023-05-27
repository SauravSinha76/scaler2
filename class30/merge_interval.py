class Interval:
    def __init__(self,s,e):
        self.start = s
        self.end = e

def solve(intervals, new_interval):
    ans =[]
    n = len(intervals)
    for i in range(n):
        if intervals[i].end < new_interval.start:
           ans.append(intervals[i])
        elif new_interval.end < intervals[i].start:
            ans.append(new_interval)
            for j in range(i,n):
                ans.append(intervals[j])
            return ans
        else:
            new_interval.start = min(new_interval.start,intervals[i].start)
            new_interval.end = max(new_interval.end, intervals[i].end)
    ans.append(new_interval)
    return ans



