function solution(s) {
    var len = s.length;
    return s.charAt((len-1)/2) + (len%2 == 0 ? s.charAt(len/2):'');
}