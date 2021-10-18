package part_stringarray;

import java.util.Scanner;

public class num1152 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        
        if(s.equals(" ") || s.equals("")) {
            System.out.print("0");
            sc.close();
            return;
        }

        if(s.length()<=1000000){
            String s1= s.trim();
            String[] s_parse = s1.split(" ");
            System.out.println(s_parse.length);
        }
        sc.close();
    }
}
