package _행렬

fun main() {
    val mod = 1_000_000_007
    var d = readlnOrNull()?.toInt() ?: return
    //graph
    // 6 7
    // 4 5
    // 2 3
    // 0 1
    val n = 8
    var graph = Array(n){ IntArray(n) }
    listOf(
        0 to 1,0 to 2, 1 to 3, 2 to 3, 2 to 4,
        3 to 4, 3 to 5, 4 to 5, 4 to 6, 5 to 6,
        5 to 7, 6 to 7
    ).forEach { (a,b) ->
        graph[a][b] = 1
        graph[b][a] = 1
    }

    fun matrix(a: Array<IntArray>, b: Array<IntArray>): Array<IntArray>{
        val matrixGraph = Array(n){IntArray(n)}

        for (i in 0 until n){
            for (j in 0 until n){
                for (k in 0 until n){
                    matrixGraph[i][j] = (matrixGraph[i][j] + (a[i][k].toLong()%mod * b[k][j].toLong()%mod).toInt())%mod
                }
            }
        }

        return matrixGraph
    }

    fun matrixPow(){
        var innerGraph = Array(n){ c-> IntArray(n){r -> if (c==r) 1 else 0} }

        while (d>0){
            if(d%2==1){
                innerGraph = matrix(innerGraph,graph)
            }
            graph = matrix(graph,graph)
            d/=2
        }
        println(innerGraph[7][7])
    }

    matrixPow()
}
