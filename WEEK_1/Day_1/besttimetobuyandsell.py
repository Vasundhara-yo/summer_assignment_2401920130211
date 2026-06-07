class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
        ans = 0
        mini = prices[0]
        for i in range(1,len(prices)):

            if prices[i]<mini:
                mini = prices[i]
            else:
                ans=max(ans , prices[i] - mini)

        return ans