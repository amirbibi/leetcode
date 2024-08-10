class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_s = curr_s = nums[0]
    
    for n in nums[1:]:
      curr_s = max(n, curr_s + n)
      max_s = max(max_s, curr_s)
    return max_s
