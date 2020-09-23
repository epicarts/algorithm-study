/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var res= new Array();
    for(i=0;i<n;i++){
        res.push(nums[i],nums[n+i])
    }
    return res;
};