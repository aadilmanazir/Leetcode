# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head, k):
            count = 0
            while head != None:
                head = head.next
                count += 1
                if count >= k:
                    return True
                
            return False
        
        if not length(head, k):
            return head
        
        start = head
        prev = None
        curr = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        start.next = self.reverseKGroup(curr, k)
        return prev
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        