package _위상정렬
// 위상 정렬 + 가중치
// 들어오는 값 graph에 저장
// 도착 도시 일때 가중치 리셋
fun main() {

    val n = readlnOrNull()?.toInt() ?: return
    val m = readlnOrNull()?.toInt() ?: return
    val que = ArrayDeque<Int>()
    val graph = Array(n+1){
        mutableListOf<Pair<Int,Int>>()
    }
    val reverseGraph = Array(n + 1) {
        mutableListOf<Pair<Int, Int>>()
    }
    // 해당 도시까지의 최소 시간 저장
    val time  = Array(n+1){0}
    val inDegree = IntArray(n+1)

    repeat(m){
        val (a,b,c) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        graph[a].add(b to c)
        reverseGraph[b].add(a to c)
        inDegree[b]+=1
    }
    val (start,end) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return

    que.add(start)
    while(que.isNotEmpty()){
        val i = que.removeFirst()
        for((next,w) in graph[i]){
            inDegree[next] -= 1
            time[next] = maxOf(time[i]+w,time[next])
            if (inDegree[next]==0) {
                que.add(next)
            }
        }
    }

    val visited = BooleanArray(n+1)
    var road = 0
    val reverseQue = ArrayDeque<Int>()
    reverseQue.add(end)
    visited[end] = true

    while (reverseQue.isNotEmpty()){
        val i = reverseQue.removeFirst()
        for((prev,w) in reverseGraph[i]){
            if (time[prev] + w == time[i]){
                road+=1
                if (!visited[prev]){
                    visited[prev] = true
                    reverseQue.add(prev)
                }
            }
        }
    }

    println(time[end])
    println(road)
}

