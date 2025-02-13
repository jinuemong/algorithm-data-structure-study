import java.util.*

fun main() {
    val n = readLine()?.toInt() ?: return
    val adjList = Array(n + 1) { mutableListOf<Int>() }

    while (true) {
        val (x, y) = readLine()?.split(" ")?.map { it.toInt() } ?: break
        if (x == -1 && y == -1) break
        adjList[x].add(y)
        adjList[y].add(x)
    }

    val scores = IntArray(n + 1) { Int.MAX_VALUE }

    fun bfs(start: Int): Int {
        val dist = IntArray(n + 1) { -1 }
        val queue: Queue<Int> = LinkedList()
        dist[start] = 0
        queue.offer(start)

        while (queue.isNotEmpty()) {
            val current = queue.poll()

            for (neighbor in adjList[current]) {
                if (dist[neighbor] == -1) {
                    dist[neighbor] = dist[current] + 1
                    queue.offer(neighbor)
                }
            }
        }

        return dist.filter { it != -1 }.maxOrNull() ?: Int.MAX_VALUE
    }

    for (i in 1..n) {
        scores[i] = bfs(i)
    }

    val minScore = scores.filter { it != Int.MAX_VALUE }.minOrNull() ?: Int.MAX_VALUE

    val candidates = scores.mapIndexed { idx, score ->
        if (score == minScore) idx else null
    }.filter{it!=null}

    println("$minScore ${candidates.size}")
    println(candidates.joinToString(" "))
}

// 1 - 2 - 3 - 4 - 5
//     4           3

// 1 - 2 - 3 -
//     |   | |
//     4  -  |
//     |     |
//     5   - |

// 1: [2]
// 2: [1,3,4]
// 3: [2,4,5]
// 4: [2,3,5]
// 5: [3,4]
