package _그래프
fun main(){
    val di = listOf(
        0 to 1,
        0 to -1,
        1 to 0,
        -1 to 0
    )

    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val graph = Array(n){
        readlnOrNull()?.map{it.digitToInt()}?.toIntArray() ?: return
    }
    val visited = Array(n){
        graph[it].copyOf() //1은벽 2는 방문
    }

    for (i in 0..<n){
        for (j in 0..<m){
            if (visited[i][j]==0){
                var count = 1
                val que = ArrayDeque<Pair<Int,Int>>()
                val backQue = mutableSetOf<Pair<Int,Int>>()
                que.add(i to j)
                for ((dx,dy) in di) {
                    val (nx,ny) = dx+i to dy+j
                    if (nx in 0..<n && ny in 0..<m&& visited[nx][ny]==1){
                        backQue.add(nx to ny)
                    }
                }
                visited[i][j] = 2
                while (que.isNotEmpty()){
                    val (cx,cy) = que.removeFirst()
                    for ((dx,dy) in di) {
                        val (nx,ny) = cx+dx to cy+dy
                        if (nx in 0..<n && ny in 0..<m){
                            if (visited[nx][ny]==1){
                                backQue.add(nx to ny)
                            }else if(visited[nx][ny]==0) {
                                que.add(nx to ny)
                                count += 1
                                visited[nx][ny] = 2
                            }
                        }
                    }
                }
                backQue.forEach { (x,y) ->
                    graph[x][y]+=count % 10
                }
            }
        }
    }

    graph.forEach {
        println(it.map{it%10}.joinToString(""))
    }
}
