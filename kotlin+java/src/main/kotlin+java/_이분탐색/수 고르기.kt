package _이분탐색
// n이 최대 10만
fun main() {
    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val graph = List(n){
        readlnOrNull()?.toInt() ?: return
    }.sorted()
    if (graph.size <2) return println(0)
    var result = Int.MAX_VALUE
    var (start,end) = 0 to 0
    while (end < n){
        if (start > end ){
            end++
            continue
        }
        val current = graph[end] - graph[start]
        if (current >= m){
            result = minOf(result,current)
            start++
        } else {
            end ++
        }
    }
    println(result)
}

// 1 2 3 4 5
//
