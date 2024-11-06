import javax.swing.tree.TreeNode

// tree
// graph의 일종이며 node와 edge로 이루어짐
// 이진 트리 구현

data class Node(
    var value: Int,
    var left: Node? = null,
    var right: Node? = null,
)
data class Tree(val root: Node)

fun preOrderTraversal(node: Node?){
    if (node ==null) return
    print("${node.value}")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
}

fun inOrderTraversal(node: Node?){
    if (node == null) return
    inOrderTraversal(node.left)
    print("${node.value}")
    inOrderTraversal(node.right)
}

fun postOrderTraversal(node: Node?){
    if (node == null) return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print("${node.value}")
}

fun main(){
    
    val a = Node(1)
    val b = Node(2)
    val c = Node(3)
    val t = Tree(a)
    a.left = b
    a.right = c
    //  1
    // 2 3
    println("Pre-order Traversal:")
    preOrderTraversal(t.root)
    println()

    println("In-order Traversal:")
    inOrderTraversal(t.root)
    println()

    println("Post-order Traversal:")
    postOrderTraversal(t.root)
    println()
}
