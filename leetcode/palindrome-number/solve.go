import (
    "strconv"
)

func isPalindrome(x int) bool {
    var str string = strconv.Itoa(x)
    
    for i := 0; i < len(str)/2; i ++ {
        if str[i] != str[len(str)-i-1] {
            return false
        }
    }
    
    return true
}
