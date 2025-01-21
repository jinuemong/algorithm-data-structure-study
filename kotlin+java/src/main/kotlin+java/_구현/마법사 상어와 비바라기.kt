package _구현// (x,y) : 0,0 -> n-1,n-1
//  n  -> 0 , - 1 -> n-1
// x,y가 n보다 크거나 같은 경우 -n
// x,y가 0보다 작은 경우 +n

// d,s를 고려한 구름 위치 이동
// 구름 위치의 값 +1
// 구름 제거 (임시)
// 물복사 마법:거리 1의 대각선이 증가하지만, 범위를 넘어선 대각선은 증가하지 않음
// 2 이상인 칸은 구름이 생기고 물의 양 -2, 방금 구름이 제거된 경우는 안생김


fun main() {
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val direct = listOf(
        //y to x
        0 to 0, // default
        0 to -1,
        -1 to -1, //대각
        -1 to 0,
        -1 to 1, //대각
        0 to 1,
        1 to 1, //대각
        1 to 0,
        1 to -1 //대각
    )

    val graph = Array(n) {
        readlnOrNull()?.split(" ")?.map { it.toInt() }?.toIntArray() ?: return
    }
    val ds = List(m) {
        val (a, b) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        a to b
    }

    var cloud = mutableListOf(
        n - 1 to 0,
        n - 1 to 1,
        n - 2 to 0,
        n - 2 to 1,
    )
    ds.forEach { (d, s) ->
        // 구름 이동
        val direction = direct[d]
        cloud.forEachIndexed { idx, it ->
            val x = (it.first + (direction.first + n)* s) % n
            val y = (it.second + (direction.second + n)* s) % n

            // 구름 이동
            cloud[idx] = x to y
            // 구름 값 증가
            graph[x][y] += 1
        }
        cloud.forEach {
            // 물 복사
            for (i in 2..8 step 2) {
                val copy = direct[i]
                val nx = copy.first + it.first
                val ny = copy.second + it.second
                if (nx in 0..<n && ny in 0..<n && graph[nx][ny] > 0) {
                    graph[it.first][it.second] += 1
                }
            }
        }

        val newCloud = mutableListOf<Pair<Int, Int>>()
        for (i in 0..<n) {
            for (j in 0..<n) {
                val new = i to j
                if (graph[i][j] >= 2 && !cloud.contains(new)) {
                    graph[i][j] -= 2
                    newCloud.add(new)
                }
            }
        }
        cloud = newCloud
    }

    println(graph.sumOf { it.sum() })
}

