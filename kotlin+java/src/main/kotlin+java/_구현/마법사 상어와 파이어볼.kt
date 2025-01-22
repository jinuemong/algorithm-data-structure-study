package _구현

fun main() {
    val direction = listOf(
        -1 to 0,
        -1 to 1,
        0 to 1,
        1 to 1,
        1 to 0,
        1 to -1,
        0 to -1,
        -1 to -1,
    )
    val (n, m, k) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val ball = Array(m) {
        readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    }.toMutableList()
    var graph = mutableMapOf<Pair<Int, Int>, MutableList<Ball>>()
    ball.forEach {
        val (r, c, m1, s, d) = it
        val current = graph[r to c] ?: mutableListOf()
        current.add(Ball(m1, s, d))
        graph[r to c] = current
    }
    repeat(k) {
        val newGraph = mutableMapOf<Pair<Int, Int>, MutableList<Ball>>()
        // 파이어볼 추가
        graph.forEach { (key, balls) ->
            val (r, c) = key
            balls.forEach {
                val (x, y) = direction[it.d]
                val nr = (r + (x+n) * it.s) % n
                val nc = (c + (y+n) * it.s) % n
                val current = newGraph[nr to nc] ?: mutableListOf()
                current.add(it)
                newGraph[nr to nc] = current
            }
        }
        graph = newGraph
        // 파이어볼 나누기
        val changedGraph =  mutableMapOf<Pair<Int, Int>, MutableList<Ball>>()
        graph.forEach { (key, balls) ->
            if (balls.size >=2) {
                val nm = balls.sumOf { it.m } / 5
                if (nm > 0) {
                    val ns = balls.sumOf { it.s } / balls.size
                    val isEven = balls.all { it.d % 2 == 1 } || balls.all { it.d % 2 == 0 }
                    val nd = if (isEven) listOf(0, 2, 4, 6) else listOf(1, 3, 5, 7)
                    nd.forEach {
                        val current = changedGraph[key] ?: mutableListOf()
                        current.add(Ball(nm, ns, it))
                        changedGraph[key] = current
                    }
                }
            }else{
                val current = changedGraph[key] ?: mutableListOf()
                current.addAll(balls)
                changedGraph[key] = balls
            }
        }
        graph = changedGraph
    }
    println(graph.values.sumOf { balls -> balls.sumOf { it.m } })
}

// ball : r,c,m,s,d
// 위치 : (r,c) 질량 : m 속력 : s 방향 : d
data class Ball(
    val m: Int,
    val s: Int,
    val d: Int,
)


