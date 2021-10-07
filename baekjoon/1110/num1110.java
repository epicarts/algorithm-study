package part_while;
import java.io.IOException;
import java.util.Scanner;

public class num1110 {
	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		int i = 0;
		int a = 0;
		int b = 0;
		int num = 0;
		String temp = "";
		String str = "";
		num = sc.nextInt();
		str = Integer.toString(num);
		if(num<10) {
			str = "0"+ Integer.toString(num);
		} else {
			str = Integer.toString(num);
		}
		while(true) {
			
			a = Integer.parseInt(str.substring(0,1));
			b = Integer.parseInt(str.substring(1,2));
			
			if(a+b<10) {
				temp = "0"+ Integer.toString(a+b);
			} else {
				temp = Integer.toString(a+b);
			}
			str = Integer.toString(b) + temp.substring(1,2);
			
			i++;
			if(Integer.parseInt(str) == num) {
				System.out.println(i);
				break;
			} 
		}
	}
}