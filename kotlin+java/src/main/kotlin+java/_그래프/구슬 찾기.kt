package _그래프

fun main() {
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val heavierGraph = Array(n + 1) { mutableListOf<Int>() }
    val lighterGraph = Array(n + 1) { mutableListOf<Int>() }

    repeat(m) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        heavierGraph[y].add(x)
        lighterGraph[x].add(y)
    }

    fun countConnected(start: Int, graph: Array<MutableList<Int>>): Int {
        val visited = BooleanArray(n + 1)
        val stack = mutableListOf(start)
        visited[start] = true
        var count = 0

        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            for (next in graph[node]) {
                if (!visited[next]) {
                    visited[next] = true
                    stack.add(next)
                    count++
                }
            }
        }
        return count
    }

    val limit = n / 2
    val result = (1..n).count { countConnected(it, heavierGraph) > limit || countConnected(it, lighterGraph) > limit }
    println(result)
}
