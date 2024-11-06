package Top_Interview


fun mySqrt(x: Int): Int {
    // O(log x) time complex
    if (x == 0) return 0
    var start = 1
    var end = x / 2 + 1
    // In this expression, end is initialized to x / 2 + 1
    // to define the upper bound of the search range for the square root.
    while (start <= end) {
        //As long as start is less than or equal to end, the search continues.
        val mid = (start + end) / 2

        if (mid == x / mid) {
            return mid
        } else if (mid < x / mid) {
            //the target value is greater than the current mid-point value.
            start = mid + 1 // for narrow the search range
            // we need to increase the lower bound of our search

        } else { // mid > target value
            //The target value is less than the current median.
            end = mid - 1 // for narrow the search range
            // we need to reduce the upper bound of our search
        }
    }
    return end
}
