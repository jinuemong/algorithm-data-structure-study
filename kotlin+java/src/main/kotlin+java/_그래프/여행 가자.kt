package _그래프
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val m = readlnOrNull()?.toInt() ?: return
    val graph = List(n+1){
        mutableListOf<Int>()
    }
    repeat(n){
        val i = it+1
        val list = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        for (k in 0..list.lastIndex){
            val j = k +1
            if (list[k] == 1){
                graph[i].add(j)
            }
        }
    }
    val di = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val visited = BooleanArray(n+1)
    for (i in 0.. graph.lastIndex){
        if (visited[i]) continue
        val currentVisited = BooleanArray(n+1)
        val que = ArrayDeque<Int>()
        que.add(i)
        visited[i] = true
        currentVisited[i] = true
        while (que.isNotEmpty()){
            val current = que.removeFirst()
            for (j in graph[current]){
                if (!visited[j]){
                    que.add(j)
                    visited[j] = true
                    currentVisited[j] = true
                }
            }
        }
        val isOk = di.all{currentVisited[it]}
        if (isOk) return println("YES")
    }

    println("NO")
}
