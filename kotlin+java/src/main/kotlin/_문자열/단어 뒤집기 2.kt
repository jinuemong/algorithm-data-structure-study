package _문자열
//
//fun main() {
//    var input = readlnOrNull() ?: return
//
//    var word = ""
//    var tag = false
//    input.forEach {
//        if (it == '<'){
//            tag = true
//            print(word.reversed())
//            word = ""
//        }
//        if (tag){
//            print(it)
//            if (it == '>'){
//                tag = false
//            }
//        } else{
//            if (it == ' '){
//                print(word.reversed()+it)
//                word = ""
//            }else {
//                word+=it
//            }
//        }
//    }
//    if (word.length > 0) print(word.reversed())
//}

fun main() {
    val input = readlnOrNull() ?: return

    val result = StringBuilder()
    val word = StringBuilder()
    var tag = false

    input.forEach { char ->
        when {
            char == '<' -> {
                result.append(word.reverse().toString())
                word.clear()
                tag = true
                result.append(char)
            }
            tag -> {
                result.append(char)
                if (char == '>') {
                    tag = false
                }
            }
            char == ' ' -> {
                result.append(word.reverse().toString())
                result.append(char)
                word.clear()
            }
            else -> {
                word.append(char)
            }
        }
    }
    result.append(word.reverse().toString())

    println(result.toString())
}
