package _이분탐색
fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val nList = readlnOrNull()?.split(" ")?.map{it.toInt()}?.sorted() ?: return
    val target = readlnOrNull()?.toInt() ?: return
    var (start,end) = 0 to nList.lastIndex
    var result = 0
    while (start < end){
        val current = nList[start] + nList[end]
        if (current == target){
            result+=1
            start+=1
            end-=1
        } else if (current > target){
            end-=1
        } else {
            start+=1
        }
    }
    println(result)
}


// 1 2 3 5 7 9 10 11 12
// 1 - 12 match
//
