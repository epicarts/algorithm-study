import java.util.Scanner;

public class num8393 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int numT = 0;
		int sum = 0;
		
		numT = sc.nextInt();
		for(int i=1;i<numT+1;i++) {
			sum = sum + i;
		}
		System.out.println(sum);
	}
}
