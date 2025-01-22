package _백트래킹// 백 트래킹

import kotlin.math.abs
fun main(){
    val n =readlnOrNull()?.toInt() ?: return
    val a = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    var result = 0
    fun permutation(len: Int, current: IntArray, visited: BooleanArray){
        if (len ==n){
            var sum =0
            for (i in 0 until n-1){
                sum+=abs(current[i]-current[i+1])
            }
            result = maxOf(result,sum)
        }
        for (i in 0 until n){
            if (visited[i]) continue
            current[len] = a[i]
            visited[i] = true
            permutation(len+1, current,visited)
            visited[i] = false // 백트레킹
        }
    }
    val visited = BooleanArray(n)
    permutation(0,IntArray(n),visited)
    println(result)
}

// 20 1 15 8 4 10
// 20 -1 + 1-15 + an-2 - an-1
// 절대값 적용
// a[0]-a[1] + a[1]-a[2] + a[2]-a[3] + a[3]-a[4] + a[4]-a[5]
// 20 1 15 4 10 8
// 19+14+11+6+2
//완전 탐색

