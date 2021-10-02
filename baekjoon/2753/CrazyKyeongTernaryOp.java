import java.util.Scanner;
import java.util.stream.IntStream;

public class CrazyKyeongTernaryOp {
	public static void main(String[] args) {
		int A = 0;
		while(true) {
			Scanner sc = new Scanner(System.in);
			A = sc.nextInt();
			if(A>0 && A<=4000) break;
		}
		System.out.println((A%4==0) ? (A%100!=0 || A%400 ==0 ? 1 : 0) : 0);
	}
}
