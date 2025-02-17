package _그래프

fun main() {
    val di = listOf(
        0 to 1,  // 오른쪽
        1 to 0,  // 아래
        0 to -1, // 왼쪽
        -1 to 0  // 위
    )
    var d = 0
    var time = 0
    val n = readlnOrNull()?.toInt() ?: return
    val k = readlnOrNull()?.toInt() ?: return
    val graph = Array(n) { IntArray(n) }

    repeat(k) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        graph[x - 1][y - 1] = 1
    }

    graph[0][0] = 2
    val que = ArrayDeque<Pair<Int, Int>>()
    que.add(0 to 0)

    val l = readlnOrNull()?.toInt() ?: return
    val directions = mutableMapOf<Int, Char>()

    repeat(l) {
        val (x, c) = readlnOrNull()?.split(" ") ?: return
        directions[x.toInt()] = c.first()
    }

    while (true) {
        time += 1
        val (dx, dy) = di[d]
        val head = que.last()
        val nx = head.first + dx
        val ny = head.second + dy

        if (nx !in 0 until n || ny !in 0 until n || graph[nx][ny] == 2) {
            println(time)
            return
        }

        que.add(nx to ny)

        if (graph[nx][ny] == 1) {
            graph[nx][ny] = 0
        } else {
            val tail = que.removeFirst()
            graph[tail.first][tail.second] = 0
        }

        graph[nx][ny] = 2

        if (directions.containsKey(time)) {
            d = if (directions[time] == 'L') (d - 1 + 4) % 4 else (d + 1) % 4
        }
    }
}
