package _스택

fun main() {
    var result = 0
    val bar = readlnOrNull() ?: return
    val stack = mutableListOf<Char>()
    for (i in 0..bar.lastIndex) {
        if (bar[i] == '(') {
            stack.add(bar[i])
        } else {
            if (bar[i - 1] == '(') {
                result += stack.size-1
            } else {
                result += 1
            }
            stack.removeLast()
        }
    }
    println(result)
}

// () 괄호안의 괄호만큼 쇠막대기 존재
// [i-1] = ( ,[i] = )인 경우 레이저
// 괄호 안의 레이저 개수 +1 만큼 쇠막대기 증가
// ( 발견 -> 다음이 )인 경우 -> 레이저
// ( 발견 -> 다음이 )가 아닌 경우 -> 쇠막대기
// 쇠막대기 발견하면 쇠막대기 저장
// 레이저 발견하면 저장된 쇠막대기 모두 + 1
//
