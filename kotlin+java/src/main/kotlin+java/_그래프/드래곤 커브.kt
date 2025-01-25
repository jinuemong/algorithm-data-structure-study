package _그래프
fun main(){
    val di = listOf(
        1 to 0,
        0 to -1,
        -1 to 0,
        0 to 1,
    )//di를 거꾸로 가면 반시계

    val n = readlnOrNull()?.toInt()?: return
    val curve = Array(n){
        readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    }
    val graph = Array(101){
        BooleanArray(101){ false }
    }
    curve.forEach {
        var (x,y) = it[0] to it[1]
        val (d,g) = it[2] to it[3]
        var diList = listOf(d)
        repeat(g){
            val newList = mutableListOf<Int>()
            newList.addAll(diList)
            for (i in diList.lastIndex downTo 0){
                val next = (diList[i] + 1 + 4)%4
                newList.add(next)
            }
            diList = newList
        }
        graph[x][y] = true
        diList.forEach {
            x += di[it].first
            y += di[it].second
            graph[x][y] = true
        }
    }
    var count = 0
    for (i in 0..99){
        for (j in 0 .. 99){
            val isTrue = listOf(
                graph[i][j],
                graph[i+1][j],
                graph[i][j+1],
                graph[i+1][j+1]
            ).all{it}
            if(isTrue) count++
        }
    }
    println(count)
}
// 방향  : 오른쪽
// 0세대 : (1,0)
// 1세대 : (1,0), (0,-1)
// 2세대 : (1,0), (0,-1), + (-1,0), (0,-1)
// 3세대 : (1,0), (0,-1), (-1,0), (0,-1),+ (-1,0), (0,1), (-1,0), (0,-1)

// 이전 세대에서 역순으로 di-1을 더하면 됨

