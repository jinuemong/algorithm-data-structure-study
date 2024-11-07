package Top_Interview


fun isAnagram(s: String, t: String): Boolean {
    val sHashMap = HashMap<Char, Int>()

    s.forEach {
        val count = sHashMap.getOrDefault(it, DEFAULT_COUNT) + 1
        sHashMap[it] = count
    }
    t.forEach {
        val count = sHashMap[it] ?: return false
        if (count <= DEFAULT_COUNT) return false
        sHashMap[it] = count - 1
    }
    // true case -> s elements contains all t elements
    return true
}

private const val DEFAULT_COUNT = 0
