package 기초

fun main() = with(System.`in`.bufferedReader()) {
    var result = ""
    val word = Array(5) { CharArray(15){' '} }
    var maxSize = 0
    repeat(5){i ->
        val input  = readLine()
        maxSize = Math.max(input.length,maxSize)
        word[i] = input.toCharArray()
    }

    repeat(maxSize){ i ->
        repeat(5){ j ->
            word[j].getOrNull(i)?.let {
                result += word[j][i]
            }
        }
    }
    print(result)
}

class MainFragment constructor(
    private val tag: String,
): Fragment(){

}
