package _문자열

fun main() {
    val (n,m) = readlnOrNull()?.split(" ")?.map{ it.toInt()} ?: return
    val nList = List(n){
        readlnOrNull()?: return
    }
    val nSet = mutableSetOf<String>()
    var maxLength = 0
    val mList = List(m){
        val mValue = readlnOrNull()?: return
        maxLength = maxOf(maxLength, mValue.length)
        mValue
    }
    nList.forEach {
        val currentMaxLength = maxOf(it.length,maxLength)
        for (i in 0..<currentMaxLength){
            nSet.add(it.slice(0..i))
        }
    }
    var cnt = 0
    mList.forEach {mValue ->
        if (mValue in nSet) cnt+=1
    }
    println(cnt)
}
