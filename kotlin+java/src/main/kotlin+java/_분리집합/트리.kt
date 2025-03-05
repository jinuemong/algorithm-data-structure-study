package _분리집합

fun main() {
    var i = 0
    while (true) {
        val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        if (n == 0 && m == 0) break
        i++

        val parent = IntArray(n + 1) { it }
        val cycle = mutableListOf<Int>()

        fun find(x: Int): Int {
            if (parent[x] != x) {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }

        fun union(x: Int, y: Int) {
            val p1 = find(x)
            val p2 = find(y)
            if (p1 != p2) {
                if (p1 > p2) {
                    parent[p1] = p2
                } else {
                    parent[p2] = p1
                }
            } else {
                cycle.add(x) // 사이클이 발생하면 해당 정점을 기록
            }
        }

        repeat(m) {
            val (a, b) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
            union(a, b)
        }

        // find 연산으로 부모 정보 갱신
        for (i in 1..n) find(i)

        val group = mutableSetOf<Int>()
        for (cycleVertex in cycle) {
            group.add(parent[cycleVertex])
        }

        var answer = 0
        for (i in 1..n) {
            if (parent[i] in group) continue // 사이클 그룹에 포함된 루트는 제외
            answer += 1
            group.add(parent[i]) // 루트를 그룹에 추가
        }

        // 출력
        when (answer) {
            0 -> println("Case ${i}: No trees.")
            1 -> println("Case ${i}: There is one tree.")
            else -> println("Case ${i}: A forest of $answer trees.")
        }
    }
}
