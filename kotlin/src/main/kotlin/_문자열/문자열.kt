package _문자열

fun main() = with(System.`in`.bufferedReader()){
    val (a,b) = readLine().split(" ")
    var result = 50

    for (i in 0..(b.length - a.length)){
        var count = 0
        for (j in a.indices){
            if (a[j] != b[i+j]){
                count++
            }
        }
        result = minOf(count,result)
    }
    print(result)
//    fun count(current: String){
//        var count = 0
//        a.forEachIndexed { index, c ->
//            if(current[index] != c){
//                count+=1
//            }
//        }
//        result = minOf(count,result)
//    }
//    fun makeResult(current: String){
//        if (current.length < a.length) return
//        count(current)
//        val prev = current.slice(1..<current.length)
//        val next = current.slice(0..<current.length-1)
//        makeResult(prev)
//        makeResult(next)
//    }
//    makeResult(b)
//    println(result)
}
