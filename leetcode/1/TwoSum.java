package leetcode;


public class TwoSum {
	public static void main(String[] args) {
		int[] nums = {2,7,11,15};
		int target = 9;
		
		Solution sol = new Solution();
		int[] result = sol.twoSum(nums, target);
		for (int i : result) {
			System.out.print(i+" ");
		}
	}
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        int n1, n2 = 0;
        for(int i = 0;i<nums.length;i++){
            n1 = nums[i];
            for(int j = 0;j<nums.length;j++){
                if(i == j){
                    continue;
                } else if(nums[i]+nums[j]==target){
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return result;
    }
}
