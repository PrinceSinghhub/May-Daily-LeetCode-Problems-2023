class Solution:
    def stoneGameII(self, piles):
        prefix_sum = list(itertools.accumulate(reversed(piles)))[::-1]
        @cache
        def dp(index, m) -> int:
            if 2 * m >= len(piles) - index:
                return prefix_sum[index]
            return max(prefix_sum[index] - dp(index + x, max(m, x))
                       for x in range(1, 2 * m + 1))
        return dp(0, 1)