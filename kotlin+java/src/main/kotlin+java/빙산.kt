
fun main(){
    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val box = Array(n){
        readlnOrNull()?.split(" ")?.map{it.toInt()}?.toIntArray() ?: return
    }
    val direction = arrayOf(
        -1 to 0,
        1 to 0,
        0 to -1,
        0 to 1
    )
    var step = 0
    var piece : Int
    do {
        piece = 0
        val visited = Array(n){ BooleanArray(m){false} }
        for (i in 0..<n){
            for (j in 0..<m){
                if (box[i][j]!=0 && !visited[i][j]){
                    piece+=1
                    val queue = mutableListOf<Pair<Int,Int>>()
                    queue.add(i to j)
                    visited[i][j] = true
                    while (queue.isNotEmpty()){
                        val (cx,cy) = queue.removeLast()
                        direction.forEach {
                            val (x,y) = cx+it.first to cy+it.second
                            if (x in 0..<n && y in 0..<m && !visited[x][y] && box[x][y]!=0){
                                queue.add(x to y)
                                visited[x][y] = true
                            }
                        }
                    }
                }
            }
        }


        // 빙산이 녹는 과정
        val melt = Array(n) { IntArray(m) { 0 } }

        // 각 칸에서 인접한 바다의 개수를 세서 빙산을 녹임
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (box[i][j] != 0) {
                    direction.forEach {
                        val (nx, ny) = i + it.first to j + it.second
                        if (nx in 0 until n && ny in 0 until m && box[nx][ny] == 0) {
                            melt[i][j] += 1  // 주변 바다가 있을 경우 그만큼 녹임
                        }
                    }
                }
            }
        }

        // 녹은 만큼 빙산 높이 갱신
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (box[i][j] != 0) {
                    box[i][j] -= melt[i][j]
                    if (box[i][j] < 0) box[i][j] = 0 // 빙산 높이가 음수로 내려가지 않도록
                }
            }
        }

        if (piece >= 2) break
        step +=1
    } while (piece>0)

    if (piece == 0) {
        println(0)
    } else {
        println(step)
    }
}
