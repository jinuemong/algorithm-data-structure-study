
// 벽은 낮에만 부술 수 있다
data class Man(val x : Int, val y: Int, val count: Int,val life:Int, val isMorning: Boolean)

import java.util.PriorityQueue

fun main() {
    val (n,m,k) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val end = n-1 to m-1

}
