
fun main(){
    // 추출
    val list = List(6) { it * it }
    println(list.slice(1..3))
    println(list.take(2))
    println(list.drop(2))
    println(list.takeWhile { it < 10 }) // 선택 후 추출
    println(list.dropWhile { it < 10 }) // 제거 후 추출

    // 집계 함수
    val list2 = (1..5).toList()
    println(list2.reduce { acc,n -> acc + n * 2}) // 누적 값 반환
    println(list2.fold(0){ acc,n -> acc+ n*2}) // 기초값 기준으로 누적 값 반환

    // 필터
    val list3 = listOf("Red","Green","Blue")
    println(list3.filter { it.length > 3 })
    println(list3.filterNot { it.length > 3 })

}
