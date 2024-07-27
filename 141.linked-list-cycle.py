# Solution 1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (not head): return False
        s = set()
        current = head
        while current.next:
          if (current.next in s):
            return True
          s.add(current.next)
          current = current.next
        return False
      
# Solution 2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      slow = head
      fast = head
      while slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if (slow == fast): return True
      return False
