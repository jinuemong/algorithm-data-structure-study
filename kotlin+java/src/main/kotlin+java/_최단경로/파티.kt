package _최단경로
import java.util.PriorityQueue
fun main() {
    // x를 찍고 돌아와야 한다
    // 즉 마을 -> x + x -> 마을의 최단 거리
    val (n,m,x) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val result = IntArray(n+1)

    val graph = Array(n+1){
        mutableListOf<Pair<Int,Int>>()
    }
    repeat(m){
        val (x,y,t) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        graph[x].add(y to t)
    }
    fun dijkstra(start:Int): IntArray{
        val weight = IntArray(n+1){Int.MAX_VALUE}
        val que = PriorityQueue<Pair<Int,Int>>(
            compareBy {it.second}
        )
        que.add(start to 0)
        weight[start] = 0
        while (que.isNotEmpty()){
            val (current,w) = que.poll()
            if (w > weight[current]) continue

            for ((next, nextW) in graph[current]){
                if (weight[current]+nextW < weight[next]){
                    weight[next] = weight[current]+ nextW
                    que.add(next to weight[next])
                }
            }
        }
        return weight
    }
    val xToResult = dijkstra(x)
    for (start in 1..n){
        val sResult = dijkstra(start)
        result[start] += sResult[x]
    }
    for (start in 1..n){
        result[start] += xToResult[start]
    }

    println(result.max())
}
