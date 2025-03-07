package _문자열

// case> abab
// a,b 다름 -> 둘중 하나 추가
// 하나의 인덱스 -1 , count +1
// b,b 같음 -> 넘기기
// a,a (중앙) 같음 -> 넘기기
// -> 틀림 !!
// 각 자리에 추가하는 경우가 아닌, 뒤에 추가하는 경우를 고려해야 함
// 방법2>
// 앞에서 부터 가장 긴 팰랜드롬을 찾고,그를 제외한 부분을 뒤에 추가한다고 생각하기
// abab -> aba이므로 b부터 추가
// abacaba -> abavaba -> 추가 x
// qwerty -> y가 가장 긴 팰린드롬 -> qwert를 뒤에 추가
fun main() {
    val st = readlnOrNull() ?: return

    for (i in 0..st.lastIndex) {
        val sub = st.substring(i)
        if (sub == sub.reversed()) {
            println(st.length + i)
            return
        }
    }
}

