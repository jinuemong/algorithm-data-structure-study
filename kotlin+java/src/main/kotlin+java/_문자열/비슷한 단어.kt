package _문자열
fun main() {
    val n = readlnOrNull()?.toInt()?: return
    val words = List(n){
        val st = readlnOrNull() ?: return
        val result = IntArray(st.length)
        val map = mutableMapOf<Char,Int>()
        for (i in st.indices){
            val key = st[i]
            val idx = map.getOrDefault(key,i)
            result[i] = idx
            map[key] = idx
        }
        result.joinToString("")
    }
    var count = 0
    for (i in 0..n-2){
        for (j in i+1..n-1){
            if (words[i]==words[j]) count++
        }
    }
    println(count)
}
