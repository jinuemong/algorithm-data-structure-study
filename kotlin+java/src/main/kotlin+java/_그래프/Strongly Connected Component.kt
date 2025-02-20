package _그래프

fun main() {
    val (v, e) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = Array(v + 1) { mutableListOf<Int>() } // 방향 그래프
    val rGraph = Array(v + 1) { mutableListOf<Int>() } // 역방향 그래프
    val visited = BooleanArray(v + 1)
    val result = mutableListOf<MutableList<Int>>()
    val stack = mutableListOf<Int>()

    repeat(e) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        graph[x].add(y)
        rGraph[y].add(x)
    }

    // 첫 번째 DFS (탐색 순서 기록)
    fun dfs(v: Int) {
        visited[v] = true
        for (next in graph[v]) {
            if (!visited[next]) {
                dfs(next)
            }
        }
        stack.add(v) // 스택에 탐색이 끝난 정점 추가
    }

    // 역방향 그래프에서 DFS (SCC 구성)
    fun redfs(v: Int, group: MutableList<Int>) {
        visited[v] = true
        group.add(v)
        for (next in rGraph[v]) {
            if (!visited[next]) {
                redfs(next, group)
            }
        }
    }

    // 방향 그래프에서 DFS 수행
    for (i in 1..v) {
        if (!visited[i]) {
            dfs(i)
        }
    }

    // visited 배열을 리셋
    visited.fill(false)

    // 두 번째 DFS (역방향 그래프에서 SCC 찾기)
    while (stack.isNotEmpty()) {
        val node = stack.removeAt(stack.size - 1)
        if (!visited[node]) {
            val group = mutableListOf<Int>()
            redfs(node, group)
            result.add(group)
        }
    }

    // SCC 그룹을 가장 작은 정점 번호 순으로 정렬
    result.sortBy { it.minOrNull() ?: Int.MAX_VALUE }

    // 출력 준비
    println(result.size) // SCC의 개수 출력
    result.forEach {
        it.sorted().forEach { node -> print("$node ") }
        println("-1") // 각 SCC의 끝에 -1 출력
    }
}
