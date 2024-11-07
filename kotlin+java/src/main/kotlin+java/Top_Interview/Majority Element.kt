package Top_Interview

private const val DEFAULT_COUNT = 0
private const val MINIMUM_ELEMENT = 1


fun majorityElement(nums: IntArray): Int {
    val elementHashMap = HashMap<Int,Int>() // key - value element - count
    var majorityElement : Pair<Int, Int> = Pair(MINIMUM_ELEMENT,DEFAULT_COUNT)

    nums.forEach {
        val currentCount =  elementHashMap.getOrDefault(it,DEFAULT_COUNT) + 1
        elementHashMap[it] = currentCount
        if(majorityElement.second < currentCount){
            majorityElement = Pair(it,currentCount)
        }
    }

    return majorityElement.first
}
