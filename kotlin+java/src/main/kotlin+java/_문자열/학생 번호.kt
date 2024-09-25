package _문자열

fun main() = with(System.`in`.bufferedReader()) {
    val students = mutableListOf<String>()
    repeat(readLine().toInt()) {
        students.add(readLine())
    }
    val number = students[0].length
    for (k in 1..number){
        val newSize = students.map {
            it.takeLast(k)
        }.toSet().size

        if (students.size == newSize){
            print(k)
            return@with
        }
    }
//    repeat(number) { idx ->
//        val newSize = students.map {
//            it.slice(idx..<number)
//        }.toSet().size
//        val expect = number - idx + 1
//        if (newSize != students.size) {
//            println(expect)
//            return@with
//        }
//    }

}
