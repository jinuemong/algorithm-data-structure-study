package _다이나믹프로그래밍
fun main(){
    val div = 1_000_000_007
    val d = readlnOrNull()?.toInt() ?: return

    // 7 8
    // 5 6
    // 3 4
    // 1 2
    val graph: List<List<Int>> = listOf(
        listOf(),
        listOf(2,3),
        listOf(1,4),
        listOf(1,4,5),
        listOf(2,3,5,6),
        listOf(3,4,6,7),
        listOf(4,5,7,8),
        listOf(5,6,8),
        listOf(6,7),
    )
    var dp = IntArray(9)
    dp[8] = 1
    repeat(d){
        val nextDp = IntArray(9)
        for (i in 1..8){
            for (prev in graph[i]){
                nextDp[i] = (nextDp[i]+dp[prev])%div
            }
        }
        dp = nextDp
    }
    println(dp[8])
}


