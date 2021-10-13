package part_stringarray;

import java.util.ArrayList;
import java.util.Scanner;

public class num10809 {
    public static void main(String[] args) {
        int[] num_arr = {-1,-1,-1,-1,-1,
                         -1,-1,-1,-1,-1,
                         -1,-1,-1,-1,-1,
                         -1,-1,-1,-1,-1,
                         -1,-1,-1,-1,-1,
                         -1};
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] str_array;
        int count = 0;
        int temp = 0;
        str_array = str.split("");
        
        for (String s : str_array) {
            arr.add((int)s.charAt(0)-97);
        }

        temp = arr.get(0);
        num_arr[arr.get(0)] = count++;
        for(int i=1;i<arr.size();i++){
            if(temp!= arr.get(i)){
                num_arr[arr.get(i)] = count;
                
            }
            temp = arr.get(i);
            count++;
        }

        for (int i : num_arr) {
            System.out.print(Integer.toString(i)+" ");
        }
    }
}
