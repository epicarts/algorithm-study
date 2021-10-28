package part_basic_math1;

import java.util.Scanner;

public class num1712 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();long b = sc.nextInt();long c = sc.nextInt();
        System.out.println(
            (b>=c) ? -1 : a/(c-b) +1
        );
        sc.close();
    }
}
