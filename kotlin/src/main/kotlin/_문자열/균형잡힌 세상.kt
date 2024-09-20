package _문자열

import java.util.Stack

fun main() {
    var input = readlnOrNull()
    while (input != "." && input != null) {
        val stack = Stack<Char>()
        var result = "yes"
        input.forEach {
            if (it == '(' || it == '['){
                stack.add(it)
            }
            if (it == ')'){
                if(stack.size >0 && stack.lastElement() == '('){
                    stack.pop()
                }else {
                    result = "no"
                }
            }
            else if (it == ']'){
                if(stack.size >0 && stack.lastElement() == '['){
                    stack.pop()
                }else {
                    result = "no"
                }
            }
        }
        if (stack.size >0) result = "no"
        println(result)
        input = readlnOrNull()
    }
}
