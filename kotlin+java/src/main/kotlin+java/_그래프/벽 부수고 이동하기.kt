package _그래프

import java.util.PriorityQueue

data class FirstMan(val x: Int, val y: Int, val count: Int, val isSave: Boolean)

fun main() {
    val di = listOf(
        0 to 1,
        0 to -1,
        1 to 0,
        -1 to 0,
    )
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n) {
        readlnOrNull()?.map { it.digitToInt() } ?: return
    }

    val dp = Array(n) {
        Array(m) {
            IntArray(2) { Int.MAX_VALUE }
        }
    }

    val end = n - 1 to m - 1
    val que = PriorityQueue<FirstMan>(
        compareBy { it.count }
    )
    // 시작은 벽을 부수지 않음
    dp[0][0][0] = 1
    que.add(FirstMan(0, 0, 1, false))
    while (que.isNotEmpty()) {
        val man = que.poll()
        if (man.x == end.first && man.y == end.second) {
            return println(man.count)
        }
        for ((dx, dy) in di) {
            val (nx, ny) = man.x + dx to man.y + dy
            if (nx in 0..<n && ny in 0..<m) {
                val isWall = graph[nx][ny] == 1
                val wallState = if(man.isSave) 1 else 0
                // 벽을 부수지 않고 이동
                if (!isWall && dp[nx][ny][wallState] > man.count+1) {
                    val nextFirstMan = FirstMan(nx, ny, man.count + 1, man.isSave)
                    que.add(nextFirstMan)
                    dp[nx][ny][wallState] = nextFirstMan.count
                }
                // 벽을 부수고 이동 + 아직 벽을 부수지 않음
                if (isWall && !man.isSave && dp[nx][ny][1] > man.count+1) {
                    val brokenFirstMan = FirstMan(nx, ny, man.count + 1, true)
                    que.add(brokenFirstMan)
                    dp[nx][ny][1]= brokenFirstMan.count
                }
            }
        }
    }

    println(-1)
}
