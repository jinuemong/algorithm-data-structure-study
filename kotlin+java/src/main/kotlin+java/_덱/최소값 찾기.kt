package _덱// l이 너무 크면 하나하나 찾을 수 없음
import java.io.*
import java.util.*
import kotlin.collections.ArrayDeque
private data class MinNode(val idx: Int, val value: Int)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val (n, l) = br.readLine().split(" ").map { it.toInt() }
    val que = ArrayDeque<MinNode>()

    var st = StringTokenizer(br.readLine())

    for (i in 0 until n) {
        val current = st.nextToken().toInt()

        if (que.isNotEmpty() && que.first().idx <= i - l) que.removeFirst()

        while (que.isNotEmpty() && que.last().value > current) que.removeLast()

        que.add(MinNode(i, current))

        bw.write("${que.first().value} ")
    }

    bw.flush()
    bw.close()
}
//val count = (map[current] ?: 0) + 1
//map[current] = count
