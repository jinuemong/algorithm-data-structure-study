// 방향이 0인 경우를 생각
// 0 : 0 To -1
// 0 방향에서 (x,y) 중
// 0이 아닌 부분의 +1은 a
// 0이 아닌 부분의 +2은 5%
// 0인 부분의 +-1은 7%
// 0인 부분의 +-2는 2%
// 0인 부분의 +=1의 0이 아닌 부분의 +1은 10%
// 0인 부분의 +=1의 0이 아닌 부분의 -1은 1%
// 범위 아웃 되면 result에 누적

fun main() {
    val di = listOf(
        0 to -1,
        1 to 0,
        0 to 1,
        -1 to 0,
    )
    val n = readlnOrNull()?.toInt() ?: return
    val graph = Array(n) {
        readlnOrNull()?.split(" ")?.map { it.toInt() }?.toIntArray() ?: return
    }
    var result = 0
    var (x, y) = n / 2 to n / 2
    var s = 1 // 2번씩 이동 후(거리) s+1

    fun saveSand(data: Triple<Int,Int,Int>){
        if (data.first in 0 until n && data.second in 0 until n){
            graph[data.first][data.second]+=data.third
        }else {
            result += data.third
        }
    }

    fun spread(d: Pair<Int,Int>){
        val sand = mutableListOf<Triple<Int,Int,Int>>()
        val isXZero = d.first == 0
        val a = graph[x][y]
        graph[x][y] = 0 // 모래 이동
        if (isXZero){
            sand.add(Triple(x,y+d.second*2,a*5/100) )
            sand.add(Triple(x+1,y,a*7/100))
            sand.add(Triple(x-1,y,a*7/100))
            sand.add(Triple(x+2,y,a*2/100))
            sand.add(Triple(x-2,y,a*2/100))
            sand.add(Triple(x+1,y+d.second,a*10/100))
            sand.add(Triple(x-1,y+d.second,a*10/100))
            sand.add(Triple(x+1,y-d.second,a*1/100))
            sand.add(Triple(x-1,y-d.second,a*1/100))
        } else {
            sand.add(Triple(x+d.first*2,y,a*5/100) )
            sand.add(Triple(x,y+1,a*7/100))
            sand.add(Triple(x,y-1,a*7/100))
            sand.add(Triple(x,y+2,a*2/100))
            sand.add(Triple(x,y-2,a*2/100))
            sand.add(Triple(x+d.first,y+1,a*10/100))
            sand.add(Triple(x+d.first,y-1,a*10/100))
            sand.add(Triple(x-d.first,y+1,a*1/100))
            sand.add(Triple(x-d.first,y-1,a*1/100))
        }
        val spreadTotal = sand.sumOf{it.third}
        val remaining = a - spreadTotal

        sand.forEach {
            saveSand(it)
        }

        if (isXZero){
            saveSand(Triple(x,y+d.second,remaining))
        }else{
            saveSand(Triple(x+d.first,y,remaining))
        }
    }

    fun moveTo(d: Pair<Int, Int>): Boolean {
        for (i in 0 until s){
            x += d.first
            y += d.second
            spread(d)
            if (x == 0 && y == 0) return true
        }
        return false
    }

    while (true) {
        di.forEachIndexed { idx,d ->
            if(moveTo(d)) return println(result)
            if (idx%2==1) s += 1
        }
    }
}
