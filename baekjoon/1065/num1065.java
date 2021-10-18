package part_func;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class num1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int chk = 0;
		int count = 0;
		for(int i=1;i<=num;i++) {
			chk = cal(i);
			if(chk == 1) {
				count++;
			}
		}
		System.out.println(count);
        sc.close();
    }

    public static int cal(int num) {
		ArrayList<Integer> arrNum = new ArrayList<>();
		HashSet<Integer> set = new HashSet<Integer>();
		int temp = 0;		
		int result = num;
		while(num != 0) {
			result = num%10;
			num = num/10;
			arrNum.add(result);
		}
        
        if(arrNum.size()>2){
            int chk = arrNum.get(0);
            for (int i = 1; i < arrNum.size(); i++) {
                if(i!=1) {
                    chk = arrNum.get(i-1);
                }
                chk = chk - arrNum.get(i);
                temp = chk;
                set.add(temp);
            }
            
            return set.size()==1 ? 1 : 0;

        } else {
            return 1;
        }
	}
}
