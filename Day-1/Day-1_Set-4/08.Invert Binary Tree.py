# 8. **Invert Binary Tree**: Invert a binary tree (mirroring it).
#     - *Input*: A binary tree
#     - *Output*: Inverted binary tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    """
    Inverts a binary tree.
    
    Time Complexity: O(n), where n is the number of nodes in the tree.
    Space Complexity: O(h), where h is the height of the tree (space used for recursion stack).
    """
    if root is None:
        return None

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Recur for the left and right subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

# Helper function to print the tree (for testing)
def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

# Test the function
# Example tree:   4
#                /   \
#               2     7
#              / \   / \
#             1   3 6   9
# Inverted tree:  4
#                /   \
#               7     2
#              / \   / \
#             9   6 3   1
tree = TreeNode(4)
tree.left = TreeNode(2, TreeNode(1), TreeNode(3))
tree.right = TreeNode(7, TreeNode(6), TreeNode(9))

inverted_tree = invert_binary_tree(tree)
print_tree(inverted_tree)
