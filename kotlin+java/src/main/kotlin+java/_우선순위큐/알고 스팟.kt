package _우선순위큐

import java.util.PriorityQueue

fun main() {
    val di = listOf(
        0 to 1,
        0 to -1,
        1 to 0,
        -1 to 0,
    )
    val (m, n) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n) {
        readlnOrNull()?.map{it.digitToInt()}?: return
    }

    // 벽을 부수는 가중치
    // 최 대값은 n==100, m ==100 인 경우 - 2이므로 100*100으로 설정
    val weight = Array(n) { IntArray(m) { 100 * 100 } }
    // 0,0 에서 m-1, n-1로 이동
    // 0은 빈 방 , 1은 벽
    val que = PriorityQueue<Triple<Int, Int, Int>>(
        compareBy { it.third }
    )
    que.add(Triple(0,0,0))
    weight[0][0] = 0
    while (que.isNotEmpty()) {
        val (cx,cy,cw) = que.poll()
        if (cx == n-1 && cy == m-1){
            println(cw)
            break
        }
        for ((dx,dy) in di){
            val (nx,ny) = cx+dx to cy+dy
            if (nx in 0..<n && ny in 0..<m){
                val nw = weight[nx][ny]
                if (graph[nx][ny]==1){
                    //벽을 부수는 경우
                    if (nw>cw+1) {
                        weight[nx][ny] = cw + 1
                        que.add(Triple(nx, ny, cw + 1))
                    }
                }else {
                    // 부수지 않고 가는 경우
                    if (nw>cw){
                        weight[nx][ny] = cw
                        que.add(Triple(nx,ny,cw))
                    }
                }
            }
        }
    }
}
