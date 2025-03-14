package _문자열
fun main() {
    var rank = 0
    val (r,c) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val result = IntArray(10)
    val temp = Array(c){
        mutableListOf<Int>()
    }
    repeat(r){
        val st = readlnOrNull()?.reversed() ?: return
        for (i in 1..<c-3){
            if (st[i]!='.'){
                temp[i].add(st[i].digitToInt())
                break
            }
        }
    }
    temp.forEach {list ->
        if (list.isNotEmpty()){
            ++rank
            list.forEach {
                result[it] = rank
            }
        }
    }
    for (i in 1..9){
        println(result[i])
    }
}
