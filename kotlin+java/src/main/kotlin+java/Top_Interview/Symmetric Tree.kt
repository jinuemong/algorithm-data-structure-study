package Top_Interview

fun isSymmetric(root: TreeNode?): Boolean {
    fun isMirror(left: TreeNode?, right: TreeNode?): Boolean {
        return when {
            left == null && right == null -> true
            left?.`val` != right?.`val` -> false
            else -> isMirror(left?.left, right?.right) &&
                    isMirror(left?.right, right?.left)
        }
    }

    return isMirror(root?.left, root?.right)
}
