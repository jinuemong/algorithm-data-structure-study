package _문자열

import java.util.Stack

fun main() {
    var cnt = 1
    while (true) {
        var result = 0
        val st = readlnOrNull() ?: return
        if (st.contains('-')) return
        val stack = Stack<Char>()
        st.forEach {
            if (it == '}' && stack.size > 0 && stack.lastElement() == '{') {
                stack.pop()
            } else {
                stack.add(it)
            }
        }
        while (stack.size > 0) {
            val (prev, next) = listOf(stack.pop(), stack.pop())
            result += if (prev == next) 1 else 2
        }
        println("${cnt}. $result")
        cnt+=1
    }

}
