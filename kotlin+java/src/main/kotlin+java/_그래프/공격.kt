package _그래프// 탑 -> x,y 좌표에 존재
// 탑 사이의 거리가 탑 사정거리(R) 안에 있다면 에너지 전송 가능
// 1 -> 2에너지 전송 시 1은 - 10 2는 +10/2
// 에너지만큼 적을 공격

fun main() {
    fun dist(start: Pair<Int, Int>, end: Pair<Int, Int>): Double {
        return Math.sqrt(
            Math.pow((start.first - end.first).toDouble(), 2.0) +
                    Math.pow((start.second - end.second).toDouble(), 2.0)
        )
    }
    // 탑의 수, 사정거리, 초기 에너지, 적 x, 적 y
    val (n, r, d, x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    // 목표까지 도달 가능한지
    val canAttack = BooleanArray(n)
    // x, y
    val top = Array(n) {
        val (cx, cy) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        if (dist(cx to cy, x to y) <= r.toDouble()) {
            canAttack[it] = true
        }
        cx to cy
    }
    val graph = Array(n) {
        mutableListOf<Int>()
    }
    for (i in 0..<n - 1) {
        for (j in i + 1..<n) {
            if (dist(top[i], top[j]) <= r.toDouble()) {
                graph[i].add(j)
                graph[j].add(i)
            }
        }
    }

    fun dfs(start: Int): Double {
        val que = ArrayDeque<Pair<Int, Double>>()

        val visited = BooleanArray(n)
        visited[start] = true
        que.add(start to d.toDouble())

        while (que.isNotEmpty()) {
            val (current, power) = que.removeFirst()
            if (canAttack[current]) return power

            for (i in graph[current]) {
                if (graph[i].isEmpty()) continue
                if (visited[i]) continue
                if (power / 2.0 == 0.0) continue
                que.add(i to power / 2.0)
                visited[i] = true
            }
        }
        return 0.0
    }

    var result = 0.0
    for (i in 0..<n) {
        result += dfs(i)
    }
    println(result)

}
