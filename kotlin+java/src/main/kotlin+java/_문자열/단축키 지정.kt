package _문자열

fun main() {
    val easySet = mutableSetOf<Char>()

    repeat(readlnOrNull()?.toInt() ?: return) {
        val option = readlnOrNull()?.split(" ")?.toMutableList() ?: return
        var flag = false

        for (i in option.indices) {
            val op = option[i]
            if (op.first().lowercaseChar() !in easySet) {
                easySet.add(op.first().lowercaseChar())
                option[i] = "[${op.first()}]" + op.substring(1)
                flag = true
                break
            }
        }

        if (!flag) {
            outer@for (i in option.indices) {
                val op = option[i]
                for (j in op.indices) {
                    if (op[j].lowercaseChar() !in easySet) {
                        easySet.add(op[j].lowercaseChar())
                        option[i] = op.substring(0, j) + "[${op[j]}]" + op.substring(j + 1)
                        break@outer
                    }
                }
            }
        }

        println(option.joinToString(" "))
    }
}
