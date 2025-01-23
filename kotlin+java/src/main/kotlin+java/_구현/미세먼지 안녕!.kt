package _구현
fun main() {
    val di1 = listOf(
        0 to 1,
        -1 to 0,
        0 to -1,
        1 to 0,
    )
    val di2 = listOf(
        0 to 1,
        1 to 0,
        0 to -1,
        -1 to 0
    )
    var air1 = 0
    var air2 = 0

    // r c t
    val (r,c,t) = readlnOrNull()?.split(" ")?.map{it.toInt()}?:return
    var graph = Array(r){
        readlnOrNull()?.split(" ")?.map{it.toInt()}?.toIntArray() ?:return
    }

    for (i in 0..<r){
        if(graph[i][0]==-1){
            air1 = i
            air2 = i+1
            break
        }
    }


    fun clean(p:Pair<Int,Int>,d:List<Pair<Int,Int>>){
        var (nx,ny) = p
        var prev = 0
        d.forEach {
            val (dx,dy) = it
            nx+=dx
            ny+=dy
            while (nx in 0..<r && ny in 0..<c && graph[nx][ny]!=-1){
                val temp = prev
                prev = graph[nx][ny]
                graph[nx][ny] = temp
                nx+=dx
                ny+=dy
            }
            nx-=dx
            ny-=dy
        }
    }

    fun spread(){
        val newGraph = Array(r){ IntArray(c){ 0 } }
        newGraph[air1][0] = -1
        newGraph[air2][0] = -1
        for (i in 0..<r){
            for (j in 0..<c){
                if (graph[i][j]>0){
                    val m =graph[i][j]/5
                    var count = 0
                    di1.forEach{
                        val (dx,dy) = it
                        val (nx,ny) = dx+i to dy+j
                        if (nx in 0..<r && ny in 0..<c && graph[nx][ny]!=-1){
                            count+=1
                            newGraph[nx][ny]+=m
                        }
                    }
                    newGraph[i][j]+=(graph[i][j]-m*count)
                }
            }
        }
        graph = newGraph
    }
    repeat(t){
        spread()
        clean(air1 to 0, di1)
        clean(air2 to 0, di2)
    }
    println(graph.sumOf{it.sum()}+2)
}

// 독립 저장.
// 리스트를 새로 만들어서
//
// 0  30 7
// -1 10 0
// -1 0 20

//  6 15 11
// -1 10 3
// -1 2 07 8 1
//0 0 0 0 0 0 0 9
//0 0 0 0 3 0 0 8
//-1 0 5 0 0 0 22 0
//-1 8 0 0 0 0 0 0
//0 0 0 0 0 10 43 0
//0 0 5 0 15 0 0 0
//0 0 40 0 0 0 20 0
