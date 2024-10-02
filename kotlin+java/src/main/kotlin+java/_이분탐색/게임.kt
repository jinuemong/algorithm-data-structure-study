package _이분탐색

fun main(){
    val (x,y) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return

    fun cal(next: Int): Int{
        return (((y+next).toDouble()*100/(x+next).toDouble())).toInt()
    }

    var start = 0
    var end = x
    var res = x
    if (cal(0)>=99){
        return println(-1)
    }
    while(start<=end){
        val mid = (start + end)/2
        if (cal(0)<cal(mid)){
            res = mid
            end = mid -1
        }else{
            start = mid+1
        }
    }
    println(res)
}
