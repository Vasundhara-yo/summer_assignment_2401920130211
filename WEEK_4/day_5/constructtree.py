class Solution:
    def buildTree(self, preorder, inorder):

        # Store inorder value -> index
        inorderMap = {}

        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        def splitTree(rootIndex, left, right):

            # No elements
            if left > right:
                return None

            # Create root
            root = TreeNode(preorder[rootIndex])

            # Find root position in inorder
            mid = inorderMap[preorder[rootIndex]]

            # Left subtree
            root.left = splitTree(
                rootIndex + 1,
                left,
                mid - 1
            )

            # Right subtree
            root.right = splitTree(
                rootIndex + (mid - left) + 1,
                mid + 1,
                right
            )

            return root

        return splitTree(0, 0, len(inorder) - 1)
