class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head: return None

    # mid
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    
    mid = slow

    # reverse
    prev = None
    curr = mid

    while curr:
      tmp = curr.next
      curr.next = prev
      prev = curr
      curr = tmp
    
    second = prev

    # merge
    first = head
    while second.next:
      tmp = first.next
      first.next = second
      first = tmp

      tmp = second.next
      second.next = first
      second = tmp
      

