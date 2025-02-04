package _다이나믹프로그래밍
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val graph = Array(n){
        readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    }
    val dp = Array(n+2){0}

    for (i in 1..n){
        val (t,p) = graph[i-1]
        dp[i+1] = maxOf(dp[i+1],dp[i])
        if (i+t>n+1) continue
        dp[i+t] = maxOf(dp[i+t],dp[i]+p)
    }
    println(dp.max())
}

//  1 2 3 4 5 6 7
// 10 10 10
//    20 20 20 202
//1일 시작 -> 4일 도착
// 시작일 , 누적금액으로 시작
// 5   4  3  2  1 1
// 50 40 30 20 10 10
//                50
