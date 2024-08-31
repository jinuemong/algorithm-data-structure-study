package 기초

fun main() = with(System.`in`.bufferedReader()){
    val (a,b,c) = readLine().split(" ")
        .map { it.toInt() }
        .sortedBy { it }
    println(b)
}
companion object {
    fun getIntent(context: Context): Intent {
        return Intent(context, ClubAddActivity::class.java)
    }
}
