package part_while;

import java.util.Scanner;

public class num1110_using_restOp_better {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i = 0;
		int num = sc.nextInt();
		int calnum = num;
		while (true) {
			calnum = (calnum % 10) * 10 + (calnum / 10 + calnum % 10) % 10;
			i++;
			if (calnum == num) {
				System.out.println(i);
				break;
			}
		}
	}
}