package part_stringarray;

import java.util.ArrayList;
import java.util.Scanner;

public class num10809 {
    public static void main(String[] args) {
        int[] num_arr = new int[26];
        for(int i = 0; i<num_arr.length;i++){
            num_arr[i] = -1;
        }
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] str_array;
        int count = 0;
        str_array = str.split("");
        
        for (String s : str_array) {
            arr.add((int)s.charAt(0)-97);
        }

        for(int i=0;i<arr.size();i++){
            if(num_arr[arr.get(i)]==-1){
                num_arr[arr.get(i)] = count;
            }
            count++;
        }

        for (int i : num_arr) {
            System.out.print(Integer.toString(i)+" ");
        }

        sc.close();
    }
}
