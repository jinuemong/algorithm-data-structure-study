package _분리집합
import java.util.*

private const val INF = 1_000_000  // 충분히 큰 값 (최대 경로값보다 커야 함)
data class Edge1719(val to: Int, val weight: Int)

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val graph = Array(n + 1) { mutableListOf<Edge1719>() }

    repeat(m) {
        val (a, b, c) = readln().split(" ").map { it.toInt() }
        graph[a].add(Edge1719(b, c))
        graph[b].add(Edge1719(a, c))
    }

    // 경로표를 저장할 배열
    val firstStep = Array(n + 1) { IntArray(n + 1) { -1 } }

    // 모든 노드에 대해 다익스트라 실행
    for (start in 1..n) {
        dijkstra(start, n, graph, firstStep)
    }

    // 결과 출력
    for (i in 1..n) {
        for (j in 1..n) {
            if (i == j) print("- ") else print("${firstStep[i][j]} ")
        }
        println()
    }
}

// 다익스트라 알고리즘
fun dijkstra(start: Int, n: Int, graph: Array<MutableList<Edge1719>>, firstStep: Array<IntArray>) {
    val dist = IntArray(n + 1) { INF }
    val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.first })  // (거리, 노드)

    dist[start] = 0
    pq.add(0 to start)

    while (pq.isNotEmpty()) {
        val (currentDist, node) = pq.poll()

        // 현재 거리보다 크면 무시
        if (currentDist > dist[node]) continue

        for ((next, weight) in graph[node]) {
            val newDist = dist[node] + weight
            if (newDist < dist[next]) {
                dist[next] = newDist
                pq.add(newDist to next)

                // 첫 번째로 가야 하는 노드 저장
                firstStep[start][next] = if (node == start) next else firstStep[start][node]
            }
        }
    }
}
