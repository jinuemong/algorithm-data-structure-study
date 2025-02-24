fun main() {
    val n = 6
    // 자신을 부모로 저장
    val parent = IntArray(n) { it }

    fun find(x: Int): Int {
        if (parent[x] != x) {
            parent[x] = find(parent[x]) // 경로 압축
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

    union(1, 2)
    union(2, 3)
    union(4, 5)
    union(3, 4)

    println(parent.joinToString(" "))

}
