package _덱

fun main() {
    val que = ArrayDeque<Int>()
    val n = readlnOrNull()?.toInt() ?: return
    repeat(n){
        val input = readlnOrNull()?.split(" ") ?: return
        when(input[0]){
            "push_front" -> {
                que.addFirst(input[1].toInt())
            }
            "push_back" -> {
                que.add(input[1].toInt())
            }
            "pop_front" -> {
                if (que.isEmpty()){
                    println(-1)
                }else{
                    println(que.removeFirst())
                }
            }
            "pop_back" -> {
                if (que.isEmpty()){
                    println(-1)
                }else{
                    println(que.removeLast())
                }
            }
            "size" -> {
                println(que.size)
            }
            "empty" -> {
                if (que.isEmpty()){
                    println(1)
                }else{
                    println(0)
                }
            }
            "front" -> {
                if (que.isEmpty()){
                    println(-1)
                }else{
                    println(que.first())
                }
            }
            "back" -> {
                if (que.isEmpty()){
                    println(-1)
                }else{
                    println(que.last())
                }
            }
        }
    }
}
