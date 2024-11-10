package test
import java.util.*

data class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun main() {
//    val integer = readlnOrNull()?.toInt() ?: return
//    val nums = readlnOrNull()
//        ?.split(" ")
//        ?.map { it.toInt() }
    val sb = StringBuilder()
    sb.append(5)
    sb.append("abc")
    println(sb)

    val arr = intArrayOf(1,2,3)

    val arr2 = IntArray(5) { 0 }
    var arr3 = IntArray(5) {
        it * 2
    }
    val n = 2
    val m = 3
    val arr4 = Array(n){
        BooleanArray(m){ false }
    }
    arr4[0][0] = true


    val list = listOf(1,2,3)
    val list2 = mutableListOf(1,2,3)

    val stack = Stack<Int>()
    stack.add(5)
    stack.pop()

    stack.add(5)
    stack.removeLast()

    val q = LinkedList<Int>()
    q.addAll(listOf(1,2,3))
    q.offer(3)
    q.poll()
    println(q)

    val deque = ArrayDeque<Int>()
    deque.addLast(1)
    deque.add(2)
    deque.removeFirst()
    deque.removeLast()
//    deque.first()
//    deque.last()

    val a = PriorityQueue<Int>()
    a.addAll(arrayOf(1,5,21,321))
    a.offer(111)
    println(a.peek())
    println(a.poll())

    val new = PriorityQueue<String> {a,b ->
        a.length.compareTo(b.length)
    }
    new.addAll(listOf("1","12","123"))
    println(new)
}


fun preOrder(node: TreeNode?){
    if (node == null) return
    println("${node.`val`}")
    preOrder(node.left)
    preOrder(node.right)
}

fun inOrder(node: TreeNode?){
    if (node == null) return
    preOrder(node.left)
    println("${node.`val`}")
    preOrder(node.right)
}

fun postOrder(node: TreeNode?){
    if (node == null) return
    preOrder(node.left)
    preOrder(node.right)
    println("${node.`val`}")
}
