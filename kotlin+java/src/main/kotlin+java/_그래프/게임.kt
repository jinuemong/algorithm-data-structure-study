package _그래프

import java.util.PriorityQueue

private data class Sejun(
    val x: Int,
    val y: Int,
    val life: Int,
)

fun main() {
    val di = listOf(0 to 1, 0 to -1, 1 to 0, -1 to 0)
    val graph = Array(501) { IntArray(501) } // 0:안전, 1:위험, 2:죽음
    val n = readlnOrNull()?.toInt() ?: return

    repeat(n) {
        val (x1, y1, x2, y2) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        val (sx, ex) = minOf(x1, x2) to maxOf(x1, x2)
        val (sy, ey) = minOf(y1, y2) to maxOf(y1, y2)

        for (i in sy..ey) {
            for (j in sx..ex) {
                graph[i][j] = 1 // 위험 지역
            }
        }
    }

    val m = readlnOrNull()?.toInt() ?: return
    repeat(m) {
        val (x1, y1, x2, y2) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        val (sx, ex) = minOf(x1, x2) to maxOf(x1, x2)
        val (sy, ey) = minOf(y1, y2) to maxOf(y1, y2)

        for (i in sy..ey) {
            for (j in sx..ex) {
                graph[i][j] = 2 // 죽음 지역
            }
        }
    }

    val dp = Array(501) { IntArray(501) { Int.MAX_VALUE } }
    val que = PriorityQueue<Sejun>(compareBy { it.life })
    que.add(Sejun(0, 0, 0))
    dp[0][0] = 0

    while (que.isNotEmpty()) {
        val (x, y, life) = que.poll()
        if (x == 500 && y == 500) {
            println(life)
            return
        }

        for ((dx, dy) in di) {
            val cx = x + dx
            val cy = y + dy

            if (cx !in 0..500 || cy !in 0..500 || graph[cy][cx] == 2) continue

            val newLife = if (graph[cy][cx] == 1) life + 1 else life
            if (newLife < dp[cy][cx]) {
                dp[cy][cx] = newLife
                que.add(Sejun(cx, cy, newLife))
            }
        }
    }
    println(-1)
}
