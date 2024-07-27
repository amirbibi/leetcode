class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        min_val = 0
        while list1 or list2:
          val1 = list1.val if list1 else 101
          val2 = list2.val if list2 else 101
          # min_val = min(val1, val2)
          
          if (val1 <= val2):
            min_val = val1
            list1 = list1.next
          else:
            min_val = val2
            list2 = list2.next

          current.next = ListNode(min_val)
          current = current.next

        return dummy.next
