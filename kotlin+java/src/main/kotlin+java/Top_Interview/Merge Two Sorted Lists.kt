package Top_Interview

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

fun hasCycle(head: ListNode?): Boolean {
    var currentNode = head
    val nodeSet = mutableSetOf<ListNode>()

    while (currentNode != null) {
        if (currentNode in nodeSet) return false

        nodeSet.add(currentNode)

        currentNode = currentNode.next
    }

    // return : not find cycle
    return true
}
