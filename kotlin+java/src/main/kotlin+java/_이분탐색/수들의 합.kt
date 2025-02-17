package _이분탐색

fun main() {
    val (n, k) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val list = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    list.sorted()
    var result = 0
    var left = 0
    var right = 0
    var currentSum = 0
    while (right < n){
        currentSum += list[right]

        while ( currentSum > k){
            currentSum -= list[left]
            left++
        }

        if (currentSum == k){
            result++
        }

        right++
    }

    println(result)
//    for (i in 0..<n){
//        var ct = 0
//        for (j in i..<n){
//            ct += list[j]
//            if (ct>=k){
//                if (ct==k) result +=1
//                break
//            }
//        }
//    }
//    println(result)
}

// 1 1 1 1
// 1 1
//   1 1
//     1 1


// 1 1 1 2 2 2 3 3 4 5
//
