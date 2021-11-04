package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class hash_nocomplete_play {
    public static void main(String[] args) {
        //String[] arr1 = {"mislav", "stanko", "mislav", "ana"};
        //String[] arr2 = {"stanko", "ana", "mislav"};
        String[] arr1 = {"mislav", "stanko", "mislav", "ana"};
        String[] arr2 = {"stanko", "ana", "mislav"};
        Solution sol = new Solution();
        System.out.println(sol.solution(arr1, arr2));
    }
}

class Solution {
    public String solution(String[] participant, String[] completion){
        /* 
        내가 푼 방법 , 그러나 효율성 부족으로 틀림 
         */
        /*
        Arrays.sort(participant);
        Arrays.sort(completion);
        ArrayList<String> arrList = new ArrayList<>();
        arrList.addAll(Arrays.asList(participant));
        for (String s : completion) {
            arrList.remove(s);
        }
        return arrList.get(0);
        */
        
        /* 
            인터넷에 검색한 풀이방법 , 생각보다 간단하네
         */
        Arrays.sort(participant);
        Arrays.sort(completion);

        int i = 0;
        for (i = 0; i < completion.length; i++){
            if (!participant[i].equals(completion[i])) {
                break;
            }
        }
            
        return participant[i];    
        
    }
}
