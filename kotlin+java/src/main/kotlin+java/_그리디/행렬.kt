package _그리디

fun main() {
    val (n, m) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val prev: Array<Array<Int>> = Array(n) {
        readlnOrNull()?.map { it.digitToInt() }?.toTypedArray() ?: return
    }
    val next: Array<Array<Int>> = Array(n) {
        readlnOrNull()?.map { it.digitToInt() }?.toTypedArray() ?: return
    }

    fun change(x: Int, y: Int) {
        for (i in x..<x + 3) {
            for (j in y..<y + 3) {
                prev[i][j] = if (prev[i][j]==1) 0 else 1
            }
        }
    }

    if ((n < 3 || m < 3) && !prev.contentDeepEquals(next)){
        return println(-1)
    }

    var cnt = 0

    for (i in 0..<n-2){
        for (j in 0..<m-2){
            if (prev[i][j]!=next[i][j]) {
                change(i, j)
                cnt+=1
            }
        }
    }
    if(prev.contentDeepEquals(next)){
        println(cnt)
    } else{
        println(-1)
    }
}
