package _문자열

fun main() {
    val st = readlnOrNull() ?: return
    val result = StringBuilder()
    var ct = 0

    for (i in st.indices) {
        if (st[i] == 'X') {
            ct++
        } else {
            if (!fillPolyomino(result, ct)) return println(-1)
            ct = 0
            result.append(".")
        }
    }

    // 마지막 남은 'X' 처리
    if (!fillPolyomino(result, ct)) return println(-1)

    println(result.toString())
}

fun fillPolyomino(result: StringBuilder, count: Int): Boolean {
    var ct = count
    while (ct > 0) {
        if (ct >= 4) {
            result.append("AAAA")
            ct -= 4
        } else if (ct >= 2) {
            result.append("BB")
            ct -= 2
        } else {
            return false
        }
    }
    return true
}
