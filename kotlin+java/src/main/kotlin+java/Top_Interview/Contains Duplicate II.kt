package Top_Interview

import kotlin.math.abs

fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
    // O(n*n) 10 ^ 10  -> O(n) or O(logn)
    for (i in 0..nums.lastIndex - 1) {
        for (j in i + 1..nums.lastIndex) {
            if (nums[i] == nums[j] && abs(i - j) <= k) return true
        }
    }
    return false
}

fun containsNearbyDuplicate2(nums: IntArray, k: Int): Boolean {
    // O(n)
    val hashMap = HashMap<Int, Int>()
    // 0 , 1, 2
    nums.forEachIndexed { i, value ->
        hashMap[value]?.let { j ->
            if (i - j <= k) return true
        }
        hashMap[value] = i
    }

    return false
}
