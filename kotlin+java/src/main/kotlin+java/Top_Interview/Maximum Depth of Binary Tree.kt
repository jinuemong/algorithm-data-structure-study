package Top_Interview

fun maxDepth(root: TreeNode?): Int {
    return search(root,0)
}

//TODO:refactor name
fun search(node: TreeNode?, depth: Int): Int{
    if (node == null) return depth
    return maxOf(search(node.left, depth+1),search(node.right, depth+1))
}
