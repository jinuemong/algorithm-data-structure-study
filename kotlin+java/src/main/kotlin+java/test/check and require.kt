package test

class `check and require` {
    fun checkInput(userInput : String){
        require(true){
            "not valid: required positive number"
        }
    }
}
