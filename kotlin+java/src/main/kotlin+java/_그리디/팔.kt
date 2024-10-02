package _그리디

fun main() {
    val (lString, rString) = readlnOrNull()?.split(" ") ?: return
    var cnt = 0

    if (lString.length == rString.length) {
        for (i in lString.indices) {
            if (lString[i] == rString[i]) {
                if (lString[i] == '8') {
                    cnt += 1
                }
            } else {
                break
            }
        }
    }
    println(cnt)
}
