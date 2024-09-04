# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class soultion:
    def addtwonumber(self,l1:optional[Listnode],l2:optional[Listnode]) -> optional[Listnode]:
        total = carry= 0
        dummy = ListNode()
        result = dummy
        
        while l1 or l2 or carray:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        return result.next