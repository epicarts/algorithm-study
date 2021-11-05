package programmers.woahan_Tech_coding_before_test;

import java.util.ArrayList;

public class wootech_coding_before_test {
    public static void main(String[] args) {
        int[][] sqr_arr = {{1, 4}, {3, 4}, {3, 10}};
        Solution sol = new Solution();
        System.out.println(sol.solution(sqr_arr));
    }
}

class Solution {
    public int[] solution(int[][] v) {
        int[] answer = new int[2];
        int flag =0;
        ArrayList<Integer> arr_x = new ArrayList<>();
        ArrayList<Integer> arr_y = new ArrayList<>();
        for(int i=0;i<v.length;i++){
            for(int j=0;j<v[i].length;j++){
                //System.out.print(v[i][j]+" ");
                if(flag==0){
                    if(!arr_x.contains(v[i][j])){
                        arr_x.add(v[i][j]);
                    } else{
                        arr_x.remove(arr_x.indexOf(v[i][j]));
                    }
                    flag=1;
                } else{
                    if(!arr_y.contains(v[i][j])){
                        arr_y.add(v[i][j]);
                    } else{
                        arr_y.remove(arr_y.indexOf(v[i][j]));
                    }
                }
            }
            flag=0;
        }
        answer[0]=arr_x.get(0);
        answer[1]=arr_y.get(0);
        return answer;
    }
}