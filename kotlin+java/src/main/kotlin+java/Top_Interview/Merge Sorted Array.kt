package Top_Interview

// sub answer
// O(nlogn) -> n = m + n O((m+n) long (m+n))
fun merge2(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
    for (j in 0 until n) {
        nums1[m + j] = nums2[j]
    }
    nums1.sort()
}

// main answer
// O(n) -> n = m+n  //O(m+n)
fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
    // track for index
    // downTo
    var nums1Index = m - 1
    var nums2Index = n - 1
    var saveIndex = m + n - 1
    // nums1 = [1,2,3,0,0,0]
    // nums2 = [2,5,6]
    while (nums2Index >= 0) {
        if (nums1Index >= 0 && nums1[nums1Index] > nums2[nums2Index]) {
            nums1[saveIndex] = nums1[nums1Index]
            nums1Index -= 1
        } else {
            nums1[saveIndex] = nums2[nums2Index]
            nums2Index -= 1
        }
        saveIndex -= 1
    }
}
