class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    l = 0
    for r in range(len(prices)):
      curr_profit = prices[r] - prices[l]
      if (prices[r] < prices[l]):
        l = r
      else:
        max_profit = max(max_profit, curr_profit)
    return max_profit
