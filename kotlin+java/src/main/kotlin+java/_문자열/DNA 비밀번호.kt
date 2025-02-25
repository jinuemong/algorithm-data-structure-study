package _문자열
fun main() {
    val (s,p) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val st = readlnOrNull()?: return
    val acgt = readlnOrNull()?.split(" ")?.map{it.toInt()}?.toIntArray() ?: return
    val current = IntArray(4)
    var count = 0
    var j = 0
    fun isValid(): Boolean{
        var isFind = true
        for (i in 0..3){
            if(acgt[i] > current[i]){
                isFind = false
                break
            }
        }
        return isFind
    }
    for (i in 0 until p) {
        when (st[i]) {
            'A' -> current[0]++
            'C' -> current[1]++
            'G' -> current[2]++
            'T' -> current[3]++
        }
    }
    if (isValid()) count++
    for (i in p until s) {
        when (st[i - p]) {
            'A' -> current[0]--
            'C' -> current[1]--
            'G' -> current[2]--
            'T' -> current[3]--
        }

        when (st[i]) {
            'A' -> current[0]++
            'C' -> current[1]++
            'G' -> current[2]++
            'T' -> current[3]++
        }
        if (isValid()) count++
    }
    println(count)
}
