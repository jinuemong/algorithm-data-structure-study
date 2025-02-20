package _최단경로

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

data class Doro(
    val cost: Int,
    val i: Int,
    val k: Int
) : Comparable<Doro> {
    override fun compareTo(other: Doro): Int = this.cost - other.cost
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m, k) = br.readLine().split(" ").map { it.toInt() }

    val dp = Array(n + 1) { IntArray(k + 1) { Int.MAX_VALUE } }
    val graph = List(n + 1) { mutableListOf<Pair<Int, Int>>() }

    repeat(m) {
        val (x, y, w) = br.readLine().split(" ").map { it.toInt() }
        graph[x].add(y to w)
        graph[y].add(x to w)
    }

    val que = PriorityQueue<Doro>(
        compareBy{it.cost}
    )
    dp[1][0] = 0
    que.add(Doro(0, 1, 0))

    while (que.isNotEmpty()) {
        val doro = que.poll()
        if (dp[doro.i][doro.k] < doro.cost) continue

        for ((next, w) in graph[doro.i]) {
            if (doro.k < k && dp[next][doro.k + 1] > doro.cost) {
                dp[next][doro.k + 1] = doro.cost
                que.add(Doro(doro.cost, next, doro.k + 1))
            }
            if (dp[next][doro.k] > doro.cost + w) {
                dp[next][doro.k] = doro.cost + w
                que.add(Doro(doro.cost + w, next, doro.k))
            }
        }
    }

    println(dp[n].minOrNull() ?: 0)
}
