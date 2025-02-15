package _최단경로

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val dp = IntArray(n+1){Int.MAX_VALUE}
    val weight = IntArray(n+1)
    val graph = Array(n+1){
        mutableListOf<Int>()
    }
    val inDegree = IntArray(n+1)

    repeat(n){
        val idx = it+1
        val list = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        weight[idx] = list[0]
        dp[idx] = list[0]
        for (i in 1..list.lastIndex){
            if (list[i] == -1) break
            graph[list[i]].add(idx)
            inDegree[idx]+=1
        }
    }
    for (i in 1..n){
        // 진입 차수
        if (inDegree[i]==0){
            // 목적지, 가중치
            val que = ArrayDeque<Pair<Int,Int>>()
            que.add(i to weight[i])
            while(que.isNotEmpty()){
                val (cx,cw) = que.removeFirst()
                for ( j in graph[cx]){
                    if (dp[j] < cw+weight[j]){
                        dp[j] = cw+weight[j]
                        que.add(j to dp[j])
                    }
                }
            }

        }
    }
    for (i in 1..n){
        println(dp[i])
    }
}
