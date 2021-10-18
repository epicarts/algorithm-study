package part_stringarray;

import java.util.Scanner;

public class num2675 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caseNum = 0;
        caseNum = sc.nextInt();
        String[] s = new String[caseNum];
        int[] loop = new int[caseNum];
        
        String[] temp_str;

        for(int i=0;i<caseNum;i++){
            loop[i] = sc.nextInt();
            s[i] = sc.nextLine();
        }

        for(int i=0;i<caseNum;i++){
            temp_str = s[i].split("");
            for(int j=1;j<temp_str.length;j++){
                for(int k=0;k<loop[i];k++){
                    System.out.print(temp_str[j]);
                }
            }
            System.out.println();
        }

        sc.close();
    }
}
