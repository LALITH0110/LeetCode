class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fake = ListNode(0)  
        current = fake 
        carry = 0  

        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0


            total = val1 + val2 + carry
            carry = total // 10  
            total = total % 10 


            current.next = ListNode(total)
            current = current.next


            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return fake.next  
