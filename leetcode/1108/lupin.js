/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    var res = address.replace(/\./g,"[\.]");
    return res;
    
};