package _스택

fun main() {
    val st = readlnOrNull() ?: return
    //괄호열
    // () -> 2
    // [] -> 3
    // ([]) -> 2*3
    // [[]] -> 3*3
    // stackdmf
    var result = 0
    var prev = 1
    val stack = mutableListOf<Char>()
    for (i in 0..st.lastIndex){
        when(st[i]){
            '(' -> {
                prev *=2
                stack.add('(')
            }
            '[' -> {
                prev *=3
                stack.add('[')
            }
            ')' -> {
                if (stack.isEmpty() || stack.last() != '(') return println(0)
                if (st[i-1] == '(') result +=prev
                stack.removeLast()
                prev/=2
            }
            ']' -> {
                if (stack.isEmpty() || stack.last() != '[') return println(0)
                if (st[i-1] == '[') result +=prev
                stack.removeLast()
                prev/=3
            }
        }
    }

    if (stack.isNotEmpty()) println(0) else println(result)
}
// (()[[]])
//   (1*2 + 1*3*3)*2
// 닫을때, 반복닫은 만큼 곱하기
// 반복닫음이 끝났으면 해당 값 더하기
// 스택이 비었으면 결과에 더하기
// prev = 2
// prev = 4
// result += 4
// prev = 2
// prev = 2*3 = 6
// prev = 2*3*3 = 18
// result += 18
// prev = 6
// prev = 2
// prev = 1
// prev *= 2
// prev*= 6
// result+=6
// prev = 2
// prev = 1
