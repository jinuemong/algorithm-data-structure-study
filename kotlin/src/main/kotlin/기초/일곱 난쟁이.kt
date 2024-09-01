package 기초

fun main() = with(System.`in`.bufferedReader()){
    val mans = mutableListOf<Int>()
        .apply {
            repeat(9) {
                add(readLine().toInt())
            }
        }
        .sortedBy { it }
    val sumMans = mans.sum()
    for ( i in 0..7) {
        for  ( j in i+1..8){
            if (sumMans - mans[i] - mans[j] == 100){
                mans.forEachIndexed { index, value ->
                    if (index != i && index != j){
                        println(value)
                    }
                }
                return@with
            }
        }
    }
}
