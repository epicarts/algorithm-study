package part_function;

public class num4673 {
	public static void main(String[] args) {
		boolean[] bol = new boolean[10001];
		
		for(int i =1;i<10001;i++) {
			int temp = d(i);
			
			if(temp < 10001) {
				bol[temp]=true;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for(int i = 1; i<10001; i++) {
			if(!bol[i]) {
				sb.append(i).append('\n');
			}
		}
		System.out.println(sb);
	}
	
	public static int d(int num) {
		int result = num;
		
		while(num != 0) {
			result = result + (num % 10);
			num = num/10;
		}
		
		return result;
	}
}

