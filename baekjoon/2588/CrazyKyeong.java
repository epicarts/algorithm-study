import java.util.Scanner;

public class CrazyKyeong {
   public static void main(String[] args) {
       int A = 0;
       int B = 0;
       int num = 0;
       int j = 1;

       Scanner sc = new Scanner(System.in);
       A = sc.nextInt();
       B = sc.nextInt();

       String B1 = Integer.toString(B);
       String[] strB = B1.split("");

       for (int i = strB.length - 1; i >= 0; i--) {
           System.out.println(A * Integer.parseInt(strB[i]));
           num += A * Integer.parseInt(strB[i]) * j;
           j = j * 10;
       }
       System.out.println(num);
   }
}
