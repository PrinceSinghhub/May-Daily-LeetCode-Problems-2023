# User function Template for python3

class Solution:
    def constructBinaryTree(self, pre, preMirror, size):

        def buildACompleetTree(pre, mirror):
            if not pre and not mirror:
                return None
            n = Node(pre[0])
            if len(pre) == 1:
                return n

            pre = pre[1:]
            mirror = mirror[1:]
            i, j = pre.index(mirror[0]), mirror.index(pre[0])
            n.left = buildACompleetTree(pre[:i], mirror[j:])
            n.right = buildACompleetTree(pre[i:], mirror[:j])
            return n

        return buildACompleetTree(pre, preMirror)