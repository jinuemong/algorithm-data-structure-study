package _그래프

fun main() {
    val di = arrayOf(
        -1 to 0,
        1 to 0,
        0 to -1,
        0 to 1
    )
    val space = mutableListOf<Pair<Int, Int>>()
    val virus = ArrayDeque<Pair<Int, Int>>()
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = Array(n) { col ->
        val rows = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        rows.forEachIndexed { row, value ->
            if (value == 2) {
                virus.add(col to row)
            } else if (value == 0) {
                space.add(col to row)
            }
        }
        rows.toIntArray()
    }
    var maxResult = 0
    for (i in 0..space.lastIndex - 2) {
        for (j in i+1..space.lastIndex - 1) {
            for (k in j+1..space.lastIndex) {
                var result = space.size - 3
                val one = space[i]
                val two = space[j]
                val three = space[k]
                val currentGraph = graph.map { it.clone() }.toTypedArray()
                val currentVirus = ArrayDeque(virus)
                currentGraph[one.first][one.second] = 1
                currentGraph[two.first][two.second] = 1
                currentGraph[three.first][three.second] = 1
                while (currentVirus.isNotEmpty()) {
                    val current = currentVirus.removeFirst()
                    di.forEach { (c, r) ->
                        val next = current.first + c to current.second + r
                        if (next.first in 0..<n && next.second in 0..<m){
                            if (currentGraph[next.first][next.second]==0){
                                result -=1
                                currentVirus.add(next)
                                currentGraph[next.first][next.second] = 2
                            }
                        }
                    }
                }
                maxResult = maxOf(result,maxResult)
            }
        }
    }
    println(maxResult)
}

// 벽을 3개 세워야 한다
// 0 중에서 3개의 벽을 세우는 경우의 수를 모두 탐색

