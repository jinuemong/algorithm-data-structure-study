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

fun main(){
    readlnOrNull()?.toInt() ?: return
    val nums = readlnOrNull()?.split(" ")?.map{it.toInt()}?: return
    val k = readlnOrNull()?.toInt() ?: return
    var holsoonWin = true
    var step = 1
}
