import java.util.Scanner;
import java.util.stream.IntStream;

public class CrazyKyeong {
	public static void main(String[] args) {
		int a = 0;
		int b = 0;
		Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		b = sc.nextInt();
		
		System.out.println(checkDimension(a,b));
	}
	
	static public int checkDimension(int a,int b) {
		return (a>0 && b>0) ? 1 : ((a<0 && b>0) ? 2 : ((a<0 && b<0) ? 3 : 4));
	}
}
