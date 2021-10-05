import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int numT = 0;
		int num1 = 0;
		int num2 = 0;
		
		numT = sc.nextInt();
		for(int i=0;i<numT;i++) {
			num1 = sc.nextInt();
			num2 = sc.nextInt();
			System.out.println(num1+num2);
		}
	}
}
