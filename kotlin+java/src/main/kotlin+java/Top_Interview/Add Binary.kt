package Top_Interview

fun addBinary(a: String, b: String): String {
    // a+ b -> 2 ->
    // 11
    //  1
    // 12
    // 20
    // 100
    // 11
    //  1
    // 12

    val (minString,maxString) =
        if (a.length > b.length) Pair(b,a)
        else Pair(a,b)

    var ab = maxString.map{ it.digitToInt()}.toIntArray()

    for(i in minString.lastIndex downTo 0){
        ab[i]+=minString[i].digitToInt()
    }

    // 12
    for (i in maxString.lastIndex downTo 1){
        if (ab[i]>=2){
            ab[i]-=2
            ab[i-1]+=1
        }
    }

    // 20 -> 00 -> 100
    val isUpper = ab[0]>=2
    if(isUpper) ab[0]-=2

    ab = if(isUpper) { intArrayOf(0)+ab} else ab

    return ab.joinToString("")
}
