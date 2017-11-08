# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, t):
        if t is None:
            return
        print(t.val)
        self.printTree(t.left)
        self.printTree(t.right)

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if
        '''
        if t1 is None:
            if t2 is None:
                return None
            t1 = TreeNode(t2.val)
            t1.left = t2
        else:
            if t2 is not None:
                t1.val = t1.val + t2.val
                self.mergeTrees(t1.left, t2.left)
                self.mergeTrees(t1.right, t2.right)
            else:
                return None
        return t1
        '''
t11 = TreeNode(1)
t12 = TreeNode(2)
t13 = TreeNode(3)
t15 = TreeNode(5)
t11.left = t13
t11.right = t12
t13.left = t15

t21 = TreeNode(1)
t22 = TreeNode(2)
t23 = TreeNode(3)
t24 = TreeNode(4)
t27 = TreeNode(7)
t22.left = t21
t22.right = t23
t21.right = t24
t23.right = t27

s = Solution()
t = s.mergeTrees(t11,t22)
s.printTree(t)
