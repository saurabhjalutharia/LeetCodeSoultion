import os
os.system("cls")

class ListNode:
    def __init__(self, x):
        self.val = x                        #NODE VALUE
        self.next = None                    #NODE LINK

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)                    #EXTRA NODE
        current, carry = dummy, 0              #SET CARRY AS ZERO DEFAULT

        while l1 or l2:                        #LOOP TILL ONE OF THE LIST GET EXHAUSTED
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val // 10, val % 10        #FOR LAST DIGI
            current.next = ListNode(val)
            current = current.next
        if carry == 1:
            current.next = ListNode(1)
        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print ("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))