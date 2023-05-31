class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        post_sum = [0]
        for s in stoneValue[::-1]:
            post_sum += post_sum[-1] + s,
        post_sum = post_sum[::-1][:-1]
        n = len(stoneValue)

        dp = [-10 ** 9] * (n - 3) + post_sum[-3:]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i], post_sum[i] - min(dp[i + j] for j in range(1, 4) if i + j < n))

        alice, bob = dp[0], post_sum[0] - dp[0]
        return 'Tie' if alice == bob else 'Alice' if alice > bob else 'Bob'