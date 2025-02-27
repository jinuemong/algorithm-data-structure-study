package _문자열

fun main() {
    repeat(readlnOrNull()?.toInt() ?: return){
        val st = readlnOrNull() ?: return
        fun check(left: Int, right: Int): Triple<Boolean,Int,Int>{
            var left = left
            var right = right
            while (left < right){
                if (st[left] != st[right]){
                    return Triple(false,left,right)
                }
                left++
                right--
            }
            return Triple(true,left,right)
        }
        val (first,left,right) = check(0,st.lastIndex)
        if (first){
            println(0)
        }else {
            val (second,_,_) = check(left+1,right)
            val (third,_,_) = check(left,right-1)
            if (second || third){
                println(1)
            }else {
                println(2)
            }
        }
    }
}
