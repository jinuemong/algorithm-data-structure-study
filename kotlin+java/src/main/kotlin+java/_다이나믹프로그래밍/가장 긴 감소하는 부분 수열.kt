package _다이나믹프로그래밍
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val nList = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val dp = Array(n){1}
    for (i in 1..<n){
        for (j in 0..<i){
            if (nList[i]< nList[j]){
                dp[i] = maxOf(dp[i],dp[j]+1)
            }
        }
    }
    println(dp.max())
}
