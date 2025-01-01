package _구현

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    readlnOrNull()?.toInt() ?: return
    val nums = readlnOrNull()
        ?.split(" ")
        ?.map { it.toInt() } ?: return
    // number , Pair<추천수, 순위>
    val picture = LinkedHashMap<Int, Int>()
    nums.map {
        val count = (picture[it] ?: 0) + 1
        if (count == 1 && picture.size >= n) {
            // 삭제 후 새로 추가
            var minKey = 0
            var minValue = 1001
            picture.forEach { (key, value) ->
                if (value < minValue){
                    minKey = key
                    minValue = value
                }
            }
            picture.remove(minKey)
        }
        picture[it] = count
    }
    println(picture.keys.sorted().joinToString(" "))
}

// 사진틀 n
// 사진틀이 가득찬 경우
// - 가장 적은 횟수 삭제
// - 가장 적은 횟수가 중복인 경우 가장 오래된 것 삭제
