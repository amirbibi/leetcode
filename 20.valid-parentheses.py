class Solution:
  def isValid(self, s: str) -> bool:
    h = {
        ')': '(',
        ']': '[',
        '}': '{'
      }
      stack = []
      for c in s:
        if (c in h):
          if (len(stack) > 0 and stack.pop() != h[c]):
            return False
        else:
          stack.append(c)
      return len(stack) == 0
