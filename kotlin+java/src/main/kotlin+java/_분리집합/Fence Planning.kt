package _분리집합

fun main() {
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val cow = Array(n + 1) { intArrayOf(Int.MAX_VALUE, Int.MIN_VALUE, Int.MAX_VALUE, Int.MIN_VALUE) }
    val parent = IntArray(n + 1) { it }
    val point = List(n) {
        readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    }

    fun find(x: Int): Int {
        if (parent[x] != x) {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    fun union(x: Int, y: Int) {
        val nx = find(x)
        val ny = find(y)
        if (nx != ny) {
            parent[ny] = nx
        }
    }


    // moo 연결
    repeat(m) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        union(x, y)
    }

    // 각 moo network에 대한 최소/최대 좌표 갱신
    for (i in 1..n) {
        val idx = find(i)
        val (cx, cy) = point[i - 1]

        cow[idx][0] = minOf(cow[idx][0], cx)  // minX
        cow[idx][1] = maxOf(cow[idx][1], cx)  // maxX
        cow[idx][2] = minOf(cow[idx][2], cy)  // minY
        cow[idx][3] = maxOf(cow[idx][3], cy)  // maxY
    }

    // 최소 둘레 구하기
    var result = Int.MAX_VALUE
    cow.forEach {
        if (it[0] != Int.MAX_VALUE) {
            val perimeter = (it[1] - it[0]) * 2 + (it[3] - it[2]) * 2
            result = minOf(result, perimeter)
        }
    }
    println(result)
}
