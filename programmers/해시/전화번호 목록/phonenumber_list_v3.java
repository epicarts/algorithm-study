package programmers.part_hash.phonenumber_list;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;

public class phonenumber_list_v3 {
    public static void main(String[] args) {
        //String[] arr = {"119", "97674223", "1195524421"};
        //String[] arr = {"123","456","789"};
        //String[] arr = {"12","123","1235","567","88"};
        //String[] arr = {"12","132123","1421335","567","88"};
        //String[] arr = {"88","2123","1422123","567","812"};
        //String[] arr = {"88","2123","1422123","567","82822222"};
        String[] arr = {"88","2123","1422123","567","8822222"};
        Solution3 sol = new Solution3();
        System.out.println(sol.Solution3(arr));
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

class Solution3 {
    public boolean Solution3(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        for(int j=0;j<phone_book.length-1;j++){
            System.out.println("phone_book[j] : " + phone_book[j]);
            System.out.println("phone_book[j+1] : " + phone_book[j+1]);
            System.out.println();
            if(phone_book[j+1].startsWith(phone_book[j]))return false;
        }
        return answer;
    }
}