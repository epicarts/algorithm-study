package part_stringarray;

import java.util.Scanner;

public class num2941 {
    public static void main(String[] args) {
        String[] except_check_arr = {"c=","c-","dz=","d-","lj","nj","s=","z="};
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        for (String s1 : except_check_arr) {
            if(s.contains(s1)){
                s=s.replace(s1, "_");
            }
        }
        System.out.println(s.length());
        sc.close();
    }
}
