import java.util.Scanner;
public class Main {
 
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int A = in.nextInt();
		int B = in.nextInt();
		
		in.close();
        
		String str = (A>B) ? ">" : ((A<B) ? "<" : "==" );
		System.out.println(str);
	}
 
}