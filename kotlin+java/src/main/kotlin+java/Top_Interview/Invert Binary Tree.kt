package Top_Interview

fun invertTree(root: TreeNode?): TreeNode? {
    if (root == null) return root

    val tempVal = root.left
    root.left = root.right
    root.right = tempVal

    invertTree(root.left)
    invertTree(root.right)

    return root
}
