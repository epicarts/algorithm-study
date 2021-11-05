package programmers.part_hash.phonenumber_list;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;

public class phonenumber_list_v2 {
    public static void main(String[] args) {
        //String[] arr = {"119", "97674223", "1195524421"};
        //String[] arr = {"123","456","789"};
        //String[] arr = {"12","123","1235","567","88"};
        String[] arr = {"12","132123","1421335","567","88"};
        //String[] arr = {"88","2123","1422123","567","812"};
        //String[] arr = {"88","2123","1422123","567","82822222"};
        //String[] arr = {"88","2123","1422123","567","8822222"};
        Solution2 sol = new Solution2();
        System.out.println(sol.Solution2(arr));
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

class Solution2 {
    public boolean Solution2(String[] phone_book) {
        boolean answer = true;
        //Comparator<String> c = new Comparator<String>() { public int compare(String s1, String s2) { return Integer.compare( s1.length(),s2.length()); } };
        //Arrays.sort(phone_book,c);
        Arrays.sort(phone_book);
        HashMap<Integer,String> map = new HashMap<>();
        for(int i=0;i<phone_book.length;i++){
            map.put(i, phone_book[i]);
        }
        int len = map.size();
        System.out.println("map 총 사이즈 : "+len);
        System.out.println("=====");
        for(int j=0;j<len-1;j++){
            String s =map.get(j);
            System.out.println("map.get(j+1) : " + map.get(j+1));
            System.out.println("s : " + s);
            System.out.println();
            if(map.get(j+1).startsWith(s)) return false;
        }
        return answer;
    }
}