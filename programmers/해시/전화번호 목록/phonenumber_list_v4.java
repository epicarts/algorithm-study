package programmers.part_hash.phonenumber_list;

import java.util.HashMap;
import java.util.Map;

public class phonenumber_list_v4 {
    public static void main(String[] args) {
        //String[] arr = {"119", "97674223", "1195524421"};
        //String[] arr = {"123","456","789"};
        //String[] arr = {"12","123","1235","567","88"};
        //String[] arr = {"12","132123","1421335","567","88"};
        //String[] arr = {"88","2123","1422123","567","812"};
        //String[] arr = {"88","2123","1422123","567","82822222"};
        String[] arr = {"88","2123","1422123","567","8822222"};
        Solution4 sol = new Solution4();
        System.out.println(sol.Solution4(arr));
        //String s1 = "가나다";
        //String s2 = "가나다";
        //System.out.println(s2.indexOf(s1));

    }
}

/* 
문제풀이 멋대로 생각해보기
1. 가장 작은 길이의 요소를 x를 찾고
2. 다른 요소가 x를 앞에 포함하는지 체크하기
 
 */

class Solution4 {
    public boolean Solution4(String[] phone_book) {
        boolean answer = true;
        
        Map<String,Integer> map = new HashMap<>();
        for(int i=0;i<phone_book.length;i++){
            map.put(phone_book[i], i);
        }

        for(int i=0;i<phone_book.length;i++){
            for(int j=0;j<phone_book[i].length();j++){
                if(map.containsKey(phone_book[i].substring(0,j))) return false;
            }
        }
        

        return answer;
    }
}