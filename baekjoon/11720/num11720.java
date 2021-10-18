package part_stringarray;

import java.util.Scanner;

public class num11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        int temp = 0;
        String num_arr;
        num_arr = sc.nextLine();
        String[] str = num_arr.split("");
        for(int i=0;i<n;i++){
            temp = temp + Integer.parseInt(str[i]);
        }

        System.out.println(temp);
        sc.close();
    }
}
