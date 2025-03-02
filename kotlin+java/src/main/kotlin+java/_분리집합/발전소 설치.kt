package _분리집합// m을 초과하지 않는, 전선을 연결할 경우 필요한 전선의 길이 * 1000 toInt()
import kotlin.math.*
import java.util.*

fun dijkstra(n: Int, limit: Double, graph: Array<Pair<Long, Long>>, connected: Array<BooleanArray>, visited: DoubleArray): Long {
    val pq = PriorityQueue<Pair<Double, Int>>(compareBy { it.first })
    pq.add(Pair(0.0, 0))
    visited[0] = 0.0

    while (pq.isNotEmpty()) {
        val cur = pq.poll()
        // 이미 최소값으로 갱신되어있다면 스킵
        if (visited[cur.second] < cur.first) continue

        // 모든 정점에 대한 거리 삽입
        for (i in 0 until n) {
            // 본인에서 본인으로 가는 경우는 스킵
            if (i == cur.second) continue

            // 두 점 사이의 거리 계산
            val nextDis = sqrt(
                (graph[i].first - graph[cur.second].first).toDouble().pow(2) +
                        (graph[i].second - graph[cur.second].second).toDouble().pow(2)
            )

            // 문제에서 주어진 연결되어있는 발전소는 가중치 0
            val newDistance = if (connected[cur.second][i]) 0.0 else nextDis

            // 제한 길이를 넘으면 스킵
            if (newDistance > limit) continue

            // 이미 방문한 점이라면, 최소 경로로 갱신되지 않으면 무시
            if (visited[i] <= cur.first + newDistance) continue

            pq.add(Pair(cur.first + newDistance, i))
            visited[i] = cur.first + newDistance
        }
    }

    // 최종 목표 지점인 n-1의 거리 반환, 1000을 곱해서 Long으로 반환
    return (visited[n - 1] * 1000).toLong()
}

fun main() = with(System.out.bufferedWriter()) {
    val br = System.`in`.bufferedReader()
    val (n, w) = br.readLine().split(' ').map { it.toInt() }
    val limit = br.readLine().toDouble()
    val graph = Array(n) { Pair(0L, 0L) }
    val connected = Array(n) { BooleanArray(n) }

    // 발전소 좌표 입력
    for (i in 0 until n) {
        val (x, y) = br.readLine().split(' ').map { it.toLong() }
        graph[i] = Pair(x, y)
    }

    // 연결된 발전소 정보 입력
    for (i in 0 until w) {
        val (from, to) = br.readLine().split(' ').map { it.toInt() }
        connected[from - 1][to - 1] = true
        connected[to - 1][from - 1] = true
    }

    // 방문 배열 초기화 (최대 값으로 설정)
    val visited = DoubleArray(n) { Double.MAX_VALUE }
    visited[0] = 0.0

    // 다익스트라 알고리즘 실행
    write("${dijkstra(n, limit, graph, connected, visited)}")
    close()
}
