import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		String str="";
		int num1 = 0;
		int num2 = 0;
		int sum = 0;
		int num = Integer.parseInt(br.readLine());
		for(int i=1;i<num+1;i++) {
			st = new StringTokenizer(br.readLine());
			num1 = Integer.parseInt(st.nextToken());
			num2 = Integer.parseInt(st.nextToken());
			sum = num1+num2;
			str = "Case #"+i+": "+num1+" + "+num2+" = ";
			bw.write(str);
			bw.write(sum+"\n");
		}
		bw.flush();
		br.close();
		bw.close();
	}
}
