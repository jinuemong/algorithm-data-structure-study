package _그래프

fun main() {
    val di = mapOf(
        "U" to (-1 to 0),
        "D" to (1 to 0),
        "L" to (0 to -1),
        "R" to (0 to 1),
    )
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n) {
        readlnOrNull()?.map{it.toString()} ?: return
    }
    val visited = Array(n) {
        IntArray(m) { 0 }
    }
    var result = 0
    for (i in 0..<n) {
        for (j in 0..<m) {
            if (visited[i][j]==0){
                val path = mutableListOf<Pair<Int,Int>>()
                var (nx,ny) = i to j
                while(true){
                    if(visited[nx][ny]==2) break // 탐색 끝난 곳
                    if (visited[nx][ny] == 1){ //세이프 존 필요
                        result++
                        for((px,py) in path) visited[px][py] = 2
                        break
                    }
                    visited[nx][ny] = 1 //현재 탐색중
                    path.add(nx to ny)

                    val (dx,dy) = di[graph[nx][ny]] ?: return
                    nx+=dx
                    ny+=dy
                }
                // 더 이상 탐색할 필요가 없음(safe 존이랑 연결된 경로) 2로 전환
                for ((px,py) in path) visited[px][py] = 2
            }
        }
    }
    // 방법 : 탐색 중에 다음이 visited가 나올 경우 하나의 safe존을 만든다.
    println(result)
    visited.forEach {
        println(it.joinToString(" "))
    }
}
