class Solution:
  def isPalindrome(self, s: str) -> bool:
    def formatString(s):
      res = ""
      for c in s:
        # c.isalnum()
        if ('A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9'):
          res += c.lower()
      return res

    res = formatString(s)
    l, r = 0, len(res) - 1
    while l < r:
      if (res[l] != res[r]): return False
      l += 1
      r -= 1
    return True
