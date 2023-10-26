# https://leetcode.com/problems/merge-intervals/
# Sort O(Nlog(N))

# simiar meta question:
# https://leetcode.com/discuss/interview-question/1675826/meta-e4e5-onsite
# Given two lists of sorted, disjoint intervals, merge them to find their union.
# Follow up: K-many lists. ((sum elements) * log(K) solution is optimal)

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    new=sorted(intervals)
    i=1
    while i<len(new):
        if new[i][0]>= new[i-1][0] and new[i][0]<=new[i-1][1]:
            new=[[min(new[i][0],new[i-1][0]), max(new[i][1],new[i-1][1])]]+new[2:]
        else:
            i+=1
    return new

def merge2(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += [i]
    return out

print(merge([[8,10],[2,6],[1,3],[1,2],[15,18]]))
print(merge2([[8,10],[2,6],[1,3],[1,2],[15,18]]))