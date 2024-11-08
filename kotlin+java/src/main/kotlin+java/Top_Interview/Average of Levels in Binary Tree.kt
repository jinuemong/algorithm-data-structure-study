package Top_Interview

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun averageOfLevels(root: TreeNode?): DoubleArray {
    val averageHashMap = HashMap<Int, Pair<Int, Long>>() // deapth, Pair<count, sumOfDeapth>

    fun bfs(node: TreeNode?, deapth: Int) {
        if (node == null) return
        var (count, sumOfDeapth) = averageHashMap.getOrDefault(deapth, Pair(0, 0))
        averageHashMap[deapth] = Pair(count + 1, sumOfDeapth + node.`val`)
        bfs(node.left, deapth + 1)
        bfs(node.right, deapth + 1)
    }

    bfs(root, 1)

    val averages = averageHashMap.values.map {
        it.second / it.first.toDouble()
    }.toDoubleArray()

    return averages
}
