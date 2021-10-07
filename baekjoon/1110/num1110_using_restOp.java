package part_while;
import java.io.IOException;
import java.util.Scanner;

public class num1110_using_restOp {
	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		int i = 0;
		int a = 0;
		int b = 0;
		int num = 0;
		int calnum = 0;
		num = sc.nextInt();
		calnum = num;
		while(true) {
			if(calnum <10) {
				a = 0;
				b = calnum;
			} else {
				a = calnum / 10;
				b = calnum % 10;
			}
			calnum = a+b;
			i++;
			calnum = b*10 + calnum%10;
			if(calnum == num) {
				System.out.println(i);
				break;
			}
		}
	}
}