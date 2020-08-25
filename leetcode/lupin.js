/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    return x === Number(x.toString().split("").reverse().join(""));
};
//splite 로 배열을 쪼갠 후 
//revsere 로 뒤집고
//join으로 문자열로 다시 변경
//Number로 값을 받아온다
//그 후 x 값과 비교하여 참인지 거짓인지 판별 
