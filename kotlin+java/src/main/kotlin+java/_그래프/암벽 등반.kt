package _그래프

import java.util.PriorityQueue

fun main() {
    val (n, t) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    // x,y -> nx,ny
    // |nx-x| <=2 && |ny-y| <=2
    // y= t인 경우까지 이동
    // 0 to 0에서 시작
    var maxX = 0
    val input = List(n) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        maxX = maxOf(maxX, x)
        y to x
    }
    val graph = Array(t + 1) {
        BooleanArray(maxX+1)
    }
    input.forEach {
        val (y, x) = it
        graph[y][x] = true
    }

    //dp[y][x]
    val dp = Array(t + 1) {
        Array(maxX+1) { Int.MAX_VALUE }
    }
    // y to x to count
    val que = PriorityQueue<Pair<Pair<Int, Int>, Int>>(
        compareBy {
            it.second
        }
    )
    que.add(0 to 0 to 0)
    dp[0][0] = 0

    while (que.isNotEmpty()) {
        val (spot, count) = que.poll()
        if (spot.first == t) continue
        for (i in spot.first - 2..spot.first + 2) {
            for (j in spot.second - 2..spot.second + 2) {
                if (i in 0..t && j in 0..maxX && graph[i][j] && count + 1 < dp[i][j]) {
                    dp[i][j] = count + 1
                    que.add(i to j to count + 1)
                }
            }
        }
    }

    val result = dp[t].min()
    println(if (result == Int.MAX_VALUE) -1 else result)
}
