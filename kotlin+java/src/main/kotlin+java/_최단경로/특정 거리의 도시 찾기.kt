package _최단경로

fun main() {
    val (n, m, k, x) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n + 1) {
        mutableListOf<Int>()
    }
    repeat(m) {
        val (p, q) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        graph[p].add(q)
    }
    val que = ArrayDeque<Pair<Int, Int>>()
    val visited = IntArray(n + 1) { Int.MAX_VALUE }

    que.add(x to 0)
    while (que.isNotEmpty()) {
        val (current, w) = que.removeFirst()
        visited[current] = minOf(w, visited[current])
        if (w == k) continue
        for (next in graph[current]) {
            if (w < k && w < visited[next]) {
                que.add(next to w + 1)
            }
        }
    }
    val result = mutableListOf<Int>()
    for (i in 1..n){
        if (visited[i] ==k) result.add(i)
    }

    if (result.isEmpty()) {
        println(-1)
    } else {
        result.forEach {
            println(it)
        }
    }
}
