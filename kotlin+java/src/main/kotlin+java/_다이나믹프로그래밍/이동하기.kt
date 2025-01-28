package _다이나믹프로그래밍
fun main() {
    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt() } ?: return
    val graph = Array(n){
        readlnOrNull()?.split(" ")?.map{it.toInt() }?.toIntArray() ?: return
    }
    for(i in 1..<n){
        graph[i][0]+=graph[i-1][0]
    }
    for (j in 1..<m){
        graph[0][j]+=graph[0][j-1]
    }
    for (i in 1..<n){
        for (j in 1..<m){
            graph[i][j] += maxOf(graph[i-1][j],graph[i][j-1])
        }
    }
    println(graph[n-1][m-1])
}
