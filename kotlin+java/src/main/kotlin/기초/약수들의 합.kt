package 기초

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val result = mutableListOf(1)
        val input = readLine().toInt()
        if (input == -1) break
        for (i in 2..Math.sqrt(input.toDouble()).toInt()){
            if (input%i ==0) {
                result.add(i)
                result.add(input / i)
            }
        }
        if (input == result.sum()){
            result.sort()
            println("$input = ${result.joinToString(" + ")}")
        }else{
            println("$input is NOT perfect.")
        }
    }
}
