package _최단경로

fun main() {
    // 키는 모두 다르다
    // 1 번 < 5번 이라면 1->5로 표현
    // 자신으로 들어오고 자신과 연결된 학생만 알 수 있다..

    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n+1){
        mutableListOf<Int>()
    }
    List(m) {
        val (a,b) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        graph[a].add(b)
    }

    val result = Array(n + 1) { r ->
        Array(n + 1) { c -> if (r == c || c==0) 1 else 0 }
    }

    fun dfs(start: Int){
        val visited = Array(n+1){false}
        val stack = mutableListOf(start)
        visited[start] = true
        while(stack.isNotEmpty()){
            val current = stack.removeLast()
            graph[current].forEach {
                if (!visited[it]) {
                    stack.add(it)
                    visited[it] = true
                    result[start][it] = 1
                    result[it][start] = 1
                }
            }
        }
    }

    for(i in 1..n){
        dfs(i)
    }
    println(result.count{it.all { it==1 }})
}
