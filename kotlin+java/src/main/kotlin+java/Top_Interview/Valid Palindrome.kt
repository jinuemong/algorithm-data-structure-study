package Top_Interview

import java.util.Locale

fun isPalindrome(s: String): Boolean {
    val letters = s
        .lowercase(Locale.getDefault())
        .filter {
            it in 'a'..'z' || it in '0'..'9'
        }
    val halfIndex = letters.length / 2 - 1
    // index : 0 1 2 3 4 5
    // ex1 > : a b c b a (odd) -> 1
    // ex2 > : a b c c b a (even) -> 2
    for (i in 0..halfIndex) { // 0, 1
        if (letters[i] != letters[letters.lastIndex - i]) return false
    }


    return true
}
