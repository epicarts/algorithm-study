package part_stringarray;

import java.util.Arrays;
import java.util.Scanner;

public class num1157 {
    public static void main(String[] args) {
        int[] alph_arr = new int[26];
        int max_count = 0;
        int max_num = 0;
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String chk_s = s.toUpperCase();
        for (int i = 0; i < chk_s.length(); i++) {
            alph_arr[chk_s.charAt(i) - 65]++;
        }

        int[] sort_arr1 = new int[26];
        for (int i = 0; i < alph_arr.length; i++) {
            sort_arr1[i] = alph_arr[i];
        }

        Arrays.sort(sort_arr1);
        for (int i = 0; i < alph_arr.length; i++) {
            if (alph_arr[i] == sort_arr1[sort_arr1.length - 1]) {
                max_count++;
                max_num = i;
            }
        }
        if (max_count > 1) {
            System.out.println("?");
        } else {
            System.out.println((char) (max_num + 65));
        }
    }
}
