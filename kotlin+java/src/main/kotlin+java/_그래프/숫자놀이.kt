package _그래프
//
//fun main(){
//    readlnOrNull()?.toInt() ?: return
//    val nums = readlnOrNull()?.split(" ")?.map{it.toInt()}?: return
//    val k = readlnOrNull()?.toInt() ?: return
//    var holsoonWin = true
//    var step = 1
//    while (true){
//        var current = step
//        var count = k
//        var currentNum = nums.size-1
//        for (i in 1..k){
//            if (nums[currentNum] <= current){
//                current -=nums[currentNum]
//                count-=1
//            }else{
//                currentNum-=1
//                if (currentNum<0){
//                    break
//                }
//            }
//            if (current==0){
//                break
//            }
//        }
//        if (current!=0){
//            if (holsoonWin){
//                println("holsoon win at $step")
//            } else {
//                println("jjaksoon win at $step")
//            }
//            break
//        }
//        step+=1
//        holsoonWin = !holsoonWin
//    }
//
//}

fun main() {
    readlnOrNull()?.toInt() ?: return
    val nums = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val k = readlnOrNull()?.toInt() ?: return
    val dp = Array(50 * 1000+1) { 0 }
    for (num in nums){
        dp[num] = 1
    }
    for (i in 1 until dp.size){
        for (num in nums){
            if (dp[i]+1 > k || i+num >= dp.size || dp[i]==0) continue
            if (dp[i+num]==0){
                dp[i+num] = dp[i] +1
            } else {
                dp[i+num] = minOf(dp[i] +1,dp[i+num])
            }
        }
    }
    for (i in 1 until dp.size){
        if (dp[i] == 0){
            if (i %2 == 0){
                println("holsoon win at $i")
            }else {
                println("jjaksoon win at $i")
            }
            break
        }
    }
}
