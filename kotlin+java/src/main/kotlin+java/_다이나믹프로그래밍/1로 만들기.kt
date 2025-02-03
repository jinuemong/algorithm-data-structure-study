
fun main(){
    val x = readlnOrNull()?.toInt() ?: return
    val dp = Array(x+1){ 1000001 }
    val prev = Array(x+1){-1}
    dp[1] = 0
    for (i in 1..<x){
        if (i*3<=x && dp[i] + 1 < dp[i * 3]){
            dp[i*3] = dp[i]+1
            prev[i*3] = i
        }
        if(i*2<=x && dp[i] + 1 < dp[i * 2]){
            dp[i*2] =dp[i]+1
            prev[i*2] = i
        }
        if (dp[i] + 1 < dp[i +1]){
            dp[i+1] = dp[i]+1
            prev[i+1] = i
        }
    }
    println(dp[x])
    val path = mutableListOf<Int>()
    var cur = x
    while (cur != -1){
        path.add(cur)
        cur = prev[cur]
    }
    println(path.joinToString(" "))
}

