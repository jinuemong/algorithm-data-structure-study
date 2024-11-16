package Top_Interview

fun removeDuplicates(nums: IntArray): Int {
    val numsSet = mutableSetOf<Int>()
    // numsSet.size  = 0
    nums.forEach {
        if(it !in numsSet){
            nums[numsSet.size] = it
            numsSet.add(it)
        }
    }


    // prev : [1,1,2]
    // next : [1,2,2]
    return numsSet.size
}
