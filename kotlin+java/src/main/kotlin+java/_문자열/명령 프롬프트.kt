package _문자열

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val fileNames = mutableListOf<String>()
    var result = ""

    for (i in 0 until n) fileNames.add(readLine())

    val nameLength = fileNames[0].length

    for (i in 0 until nameLength) { // 1
        var flag = true // 2
        val target = fileNames[0][i] // 3
        for (j in 1 until n) { // 4
            if (target != fileNames[j][i]) { // 5
                flag = false
                break
            }
        }
        result += if (flag) target // 6
        else "?"
    }

    println(result)

}
