class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(l, r):
            res = -10**31
            for c in cuts:
                if l < c < r:
                    res = min(res, r - l + dfs(l, c) + dfs(c, r))
            res = 0 if res == res else res
            return res
        return dfs(0, n)