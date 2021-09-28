import java.util.Scanner;
import java.util.stream.IntStream;

public class CrazyKyeongLambda {
	public static void main(String[] args) {
		int A = 0;
		while(true) {
			Scanner sc = new Scanner(System.in);
			A = sc.nextInt();
			if(A>0 && A<=4000) break;
		}
		if(IntStream.of(A)
				.filter(i->i%4==0)
				.filter(i->i%100!=0 || i%400==0)
				.sum()>0) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}
}
