# Definition for singly-linked list.
class LitNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        while l1 != None:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        num2 = 0
        while l2 != None:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num = num1 + num2
