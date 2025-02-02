
// 계단은 하나, 두개 씩 이동 가능
// 시작점을 제외한 연속된 세 개의 계단을 모두 밟으면 안된다
// 마지막 도착 계단은 반드시 밟아야 한다
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val nm  = List(n){
        readlnOrNull()?.toLong() ?: return
    }
    val dp = Array(n){ 0L }
    if(n==1) return println(nm[0])
    if(n==2) return println(nm.sum())
    dp[0] = nm[0]
    dp[1] = nm[0]+nm[1]
    dp[2] = maxOf(nm[0]+nm[2], nm[1]+nm[2])
    for (i in 3..<n){
        dp[i] = maxOf(dp[i-3]+nm[i-1]+nm[i],dp[i-2]+nm[i])
    }
    println(dp.last())
}

