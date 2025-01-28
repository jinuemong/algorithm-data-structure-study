import kotlin.math.pow

fun main() {
    val di = listOf(
        0 to 1,
        1 to 0,
        0 to -1,
        -1 to 0,
    )
    // 격자를 2^L, 2^L 크기로 나눔
    // 모든 격자 90도 회전
    // 90도 회전이란, 각 n/2의 격자의 자리 90도로 회전
    // 3이상 얼음이 인접해 있지 않는 칸의 얼음은 1 감소
    // 인접은 상하좌우

    // 출력
    // 남은 얼음의 합
    // 0을 만나지 않는, 가장 큰 덩어리의 수
    val (n, q) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val m = 2.toDouble().pow(n).toInt()
    var graph = Array(m) {
        readlnOrNull()?.split(" ")?.map { it.toInt() }?.toIntArray() ?: return
    }
    val storm = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return

    fun applyStorm(l: Int) {
        val size = 2.toDouble().pow(l).toInt()
        val newGraph = Array(m) { IntArray(m) }
        for (i in 0 until m step size) {
            for (j in 0 until m step size) {
                for (x in 0 until size) {
                    for (y in 0 until size) {
                        newGraph[i + y][j + size - 1 - x] = graph[i + x][j + y]
                    }
                }
            }
        }
        graph = newGraph
    }

    fun ball() {
        val newGraph = Array(m){graph[it].copyOf()}
        for (i in 0..<m) {
            for (j in 0..<m) {
                if (graph[i][j] == 0) continue

                val count = di.count {
                    val nx = i + it.first
                    val ny = j + it.second
                    nx in 0..<m && ny in 0..<m && graph[nx][ny] != 0
                }
                if (count < 3) newGraph[i][j] = graph[i][j] - 1
            }
        }
        graph = newGraph
    }

    fun bfsResult() {
        var count = 0
        var result = 0
        val visited = Array(m) {
            BooleanArray(m) { false }
        }
        for (i in 0..<m) {
            for (j in 0..<m) {
                count += graph[i][j]
                if (!visited[i][j] && graph[i][j] != 0) {
                    var current = 0
                    val queue = ArrayDeque<Pair<Int, Int>>()
                    queue.add(i to j)
                    visited[i][j] = true
                    while (queue.isNotEmpty()) {
                        current += 1
                        val (x, y) = queue.removeFirst()
                        for ((dx, dy) in di) {
                            val (nx, ny) = x + dx to y + dy
                            if (nx in 0..<m && ny in 0..<m && !visited[nx][ny] && graph[nx][ny] != 0) {
                                queue.add(nx to ny)
                                visited[nx][ny] = true
                            }
                        }
                    }
                    result = maxOf(result, current)
                }
            }
        }
        println(count)
        println(result)
    }

    storm.forEach {
        applyStorm(it)
        ball()
    }
    bfsResult()
}
