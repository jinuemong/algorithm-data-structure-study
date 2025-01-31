package _다이나믹프로그래밍
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val nm = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val dp = nm.toIntArray()

    for (i in 1..<n){ //이번에 선택할 수
        for ( j in 0..i){
            if (nm[i]>nm[j]){
                dp[i] = maxOf(dp[j]+nm[i],dp[i])
            }
        }
    }
    println(dp.max())
}
