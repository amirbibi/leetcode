# Solution 1
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if (not head): return
    
    dummy = ListNode(head.val)
    current = head
    
    while current.next != None:
      current = current.next
      node = ListNode(current.val)
      node.next = dummy
      dummy = node
    
    return dummy

# Solution 2
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = None
    while head:
        temp = head.next
        head.next = dummy
        dummy = head
        head = temp
    return dummy
