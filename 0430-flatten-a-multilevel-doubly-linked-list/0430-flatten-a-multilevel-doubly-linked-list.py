"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(head):
            if head == None:
                return None
            curr = head
            while curr != None:
                if curr.child:
                    temp_next = curr.next
                    recursive_flatten = helper(curr.child)
                    
                    recursive_end = recursive_flatten
                    while recursive_end.next != None:
                        recursive_end = recursive_end.next
                        
                    curr.next = recursive_flatten
                    recursive_flatten.prev = curr
                    recursive_end.next = temp_next
                    
                    if temp_next:
                        temp_next.prev = recursive_end
                        
                    curr.child = None
                    
                    curr = temp_next
                else:
                    curr = curr.next
                    
            return head
        
        res = helper(head)
        # for n in res:
        #     print(n.prev, "<--", n.val, "-->", n.next)
        return res

