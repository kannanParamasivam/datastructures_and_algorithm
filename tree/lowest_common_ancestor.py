'''
236. Lowest Common Ancestor of a Binary Tree
Medium

3129

164

Add to List

Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''

from collections import namedtuple
from helpers import TreeHelper, Node


Status = namedtuple('Status', ('num_target_nodes', 'ancestor'))


class Solution:

    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
        status = self.lca_helper(root, p, q)
        return status.ancestor

    def lca_helper(self, root: Node, p: Node, q: Node) -> Status:

        if not root:
            return Status(num_target_nodes=0, ancestor=None)

        left_status = self.lca_helper(root.left, p, q)

        if left_status.num_target_nodes == 2:
            return left_status

        right_status = self.lca_helper(root.right, p, q)

        if right_status.num_target_nodes == 2:
            return right_status

        return Status(num_target_nodes=left_status.num_target_nodes + right_status.num_target_nodes + (p.val, q.val).count(root.val), ancestor=root)


sol = Solution()
tree: Node = TreeHelper.create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, ])
# ancestor = sol.lowestCommonAncestor(tree, Node(5, None, None), Node(1, None, None))
ancestor = sol.lowestCommonAncestor(tree, Node(5, None, None), Node(4, None, None))
print(ancestor.val)

