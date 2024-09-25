package 기초

fun main() = with(System.`in`.bufferedReader()){
    repeat(100){
        println(readlnOrNull() ?: return@repeat)
    }
}
