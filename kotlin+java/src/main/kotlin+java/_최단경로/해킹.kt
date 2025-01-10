package _최단경로

fun main() {
    repeat(readlnOrNull()?.toInt() ?: return) {
        val (n, d, c) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        val graph = Array(n + 1) {
            mutableListOf<Pair<Int, Int>>()
        }
        val visited = IntArray(n + 1) { Int.MAX_VALUE } // 누적값 저장

        repeat(d) {
            val (a, b, s) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
            graph[b].add(a to s)
        }
        // 다음 노드 , 누적값
        val queue = ArrayDeque<Pair<Int, Int>>()
        queue.add(c to 0)
        visited[c] = 0

        while (queue.isNotEmpty()) {
            val (ci, cp) = queue.removeFirst()
            graph[ci]
                .forEach { (cn, ct) ->
                    val nextValue = cp + ct
                    if (visited[cn] == Int.MAX_VALUE){ // 등록
                        queue.add(cn to nextValue)
                        visited[cn] = nextValue
                    } else if (nextValue < visited[cn]) { // 교체
                        queue.add(cn to nextValue)
                        visited[cn] = nextValue
                    }
                }
        }
        var num  = 0
        var time = 0
        visited.forEach {
            if (it!= Int.MAX_VALUE){
                num+=1
                time = maxOf(it,time)
            }
        }
        println("$num $time")
    }
}

//1 -> 2 (2)
// 1 -> 3 (8)
// 2 -> 3 (4)
// 1
// a b

// 이미 감염된 경우는 감염시킬 수없다
// 즉 시간이 적게 걸리는 것이 우선으로 감염된다
