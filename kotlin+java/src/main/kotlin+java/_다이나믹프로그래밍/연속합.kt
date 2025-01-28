package _다이나믹프로그래밍
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val nx = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val dp = Array(n){0}
    dp[0] = nx[0]
    for (i in 1..nx.lastIndex){
        // 현재값이 더 큰 순간 부터는 더할 필요가 없음
        dp[i] = maxOf(dp[i-1] + nx[i],nx[i])
    }
    println(dp.max())

}

// -35, 12, 21, -1
// -35,
