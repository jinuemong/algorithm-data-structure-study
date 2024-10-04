package _그래프

import java.util.*

fun main() {
    val (n, m, k) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n) {
        BooleanArray(m) { false }
    }

    repeat(k) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        graph[x-1][y-1] = true
    }

    var cnt = 1
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (graph[i][j]) {
                val stack = Stack<Pair<Int,Int>>()
                var currentCount = 0
                stack.add(Pair(i,j))
                graph[i][j] =  false
                while (stack.isNotEmpty()){
                    val (x,y) = stack.pop()
                    currentCount+=1
                    for ((dx,dy) in listOf(listOf(0,1),listOf(1,0),listOf(-1,0),listOf(0,-1))){
                        val (nextX,nextY)  = Pair(x+dx,y+dy)
                        if((nextX in 0 until n) && (nextY in 0 until m) && graph[nextX][nextY]){
                            stack.add(Pair(nextX,nextY))
                            graph[nextX][nextY] = false
                        }
                    }
                }
                cnt = maxOf(cnt,currentCount)
            }
        }
    }
    println(cnt)
}
