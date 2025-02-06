package _위상정렬

fun main() {
    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val queue = ArrayDeque<Int>()

    val inDegree = Array(n+1){0}
    val graph = List(n+1){
        mutableListOf<Int>()
    }
    List(m){
        val (x,y) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        inDegree[y]+=1
        graph[x].add(y)
    }
    for (i in 1..n){
        if(inDegree[i]==0){
            queue.add(i)
        }
    }
    val result = mutableListOf<Int>()
    while(queue.isNotEmpty()){
        val current = queue.removeFirst()
        result.add(current)
        for (next in graph[current]){
            inDegree[next]-=1
            if (inDegree[next]==0){
                queue.add(next)
            }
        }
    }
    println(result.joinToString(" "))
}

// 1 3
// 2 3
// 3

// inDegree
// 1 - (0)
// 2 - (0)
// 3- 1,2 (2)
//
