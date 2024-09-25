package 기초

fun main() = with(System.`in`.bufferedReader()){
    val t = readLine().toInt()
    for (i in 0 until t){
        val (a,b) = readLine().split(" ").map { it.toInt() }
        var result = a % 10
        repeat(b-1) {
            result *=a
            result%=10
        }
        if (result == 0) println(10) else println(result)
    }
}
