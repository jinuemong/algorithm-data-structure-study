package _행렬

// 행렬 거듭제곱 문제 풀이
// N = 3으로 생각
//   1 2 3
// 1 0 1 0
// 2 1 0 1
// 3 0 1 0
// 시간이 한번 지난 경우
//

fun main() {
    val div = 1_000_000_007
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    var graph = Array(n) {
        IntArray(n)
    }

    repeat(m) {
        val (x, y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        graph[x - 1][y - 1] = 1
        graph[y - 1][x - 1] = 1
    }
    var d = readlnOrNull()?.toInt() ?: return

    fun matrix(a: Array<IntArray>, b: Array<IntArray>): Array<IntArray> {
        val newGraph = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                for (k in 0 until n) {
                    newGraph[i][j] = (newGraph[i][j] + (a[i][k].toLong()%div * b[k][j].toLong()%div)).toInt()%div
                }
            }
        }
        return newGraph
    }

    fun matrixPower() {
        // 단위 행렬 생셩
        // 행렬의 곱셈에서 항등 역할
        var result = Array(n) { c -> IntArray(n) { r -> if (r == c) 1 else 0 } }
        // d = 13인 경우
        // 이진수로 1101의 마지막 자리부터 시작
        // 2^3 + 2^2 + 2^0
        // 즉 result에 2^0 , 2^2, 2^3을 각 곱해준다

        while (d > 0) {
            if (d % 2 == 1) { // 홀수
                //홀수인 경우 result 행렬에 graph를 곱함
                result = matrix(result, graph)
            }
            // 짝수인 경우 행렬 제곱
            // graph 행렬을 자기 자신과 급해서 graph의 2^k 번째 거듭제곱을 구함
            graph = matrix(graph,graph)
            // 이진 거듭제곱 진행
            d /= 2
        }
        println(result[0][0])
    }
    matrixPower()
}
