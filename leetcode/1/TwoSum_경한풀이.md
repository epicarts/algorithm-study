Leetcode 문제 풀이
=============
문제 : Two Sum
---------

> 주소 : https://leetcode.com/problems/two-sum/ <br>
> 언어 : JAVA 11
<br>

## 1. 문제
```
Given an array of integers nums and an integer target, <br> 
return indices of the two numbers such that they add up to target. <br>
You may assume that each input would have exactly one solution, and you <br>
may not use the same element twice. You can return the answer in any order.


주어진 정수 배열과 정수 타겟으로 , 합해서 타겟 정수가 되는 두 숫자의 인덱스들을 반환하라
너는 각각의 입력값이 정확히 한개의 해결책이 있다고 볼수 있고 너는 같은 요소를 두번 사용해서는 안된다.
값은 어떠한 순서로든 반환할수 있다.
```

## 2. 문제 풀기전 알고리즘 생각
*for문 두개와 각각 i,j 인덱스를 두어 i, j 가 동일한 경우를 제외하고 모든 숫자를 한번씩 다 서로 더해본다음. target 정수가 될때 탈출한다.


## 3. 문제 코드

```
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
```

## 4. 문제 소감

- leetcode 얼마전에 알게되어서 leetcode는 아무도 안풀었겠지? 하면서 신나서 풀고 커밋하려고 왔는데 다들 많이 풀었네 ㅋㅋㅋㅋ 역시 대단
