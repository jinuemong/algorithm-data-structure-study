

// 최장 증가 수열의 시간을 단축하기 위한 LIS 알고리즘
// 실제 배열과 일치하지 않지만, 길이는 같게 구할 수있음
fun main(){
    val arr = listOf(2,1,3,5,4)
    val n = arr.size
    val list = IntArray(n)
    // 알고리즘 없는 로직
    // 초기값을 넣음 : arr[0]
    // [2]
    // arr[1]이 list의 어디에 들어가는 지 확인
    // 가장 마지막 값인 2보다 작으므로 인덱스 0과 교체
    // [1]
    // arr[2]를 확인
    // 가장 마지막 값인 1보다 크므로 삽입
    // [1, 3]
    // 5역시 가장 마지막 값보다 크므로 삽입
    // [1, 3, 5]
    // 4는ㄴ 마지막 값보다 작으므로 교체
    // [1,3, 4]

    // 이분 탐색으로 숫자가 들어갈 위치를 찾음
    // list는 기본적으로 증가 수열 -> 정렬 됭
    // 들어갈 위치는 현재 수보다 크거나 같은 값
    fun binarySearch(left: Int, right: Int, target: Int): Int{
        var left = left
        var right = right
        var mid: Int

        while (left < right){
            mid = (left+right)/2

            if (list[mid] < target){
                left = mid+1
            } else{
                right = mid
            }
        }
        return right
    }

    list[0] = arr[0]
    var i = 1 // arr
    var j = 0 // 리스트의 인덱스
    while ( i <n){
        // 다음 값이 마지막 값보다 큰 경우
        // 마지막에 추가
        if (list[j] < arr[i]){
            list[j+1] = arr[i]
            j+=1
        }
        // 같거나 작은 경우
        // 가장 근접한 수와 교체 알고리즘
        else {
            val idx = binarySearch(0,j,arr[i])
            list[idx] = arr[i]
        }
        i+=1
    }
    println(j+1)

}
