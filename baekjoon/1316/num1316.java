package part_stringarray;

import java.util.Scanner;

public class num1316 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        int group_count = 0;
        sc.nextLine();
        for(int i=0;i<cnt;i++){
            group_count += chk_group_word(sc.nextLine());
        }
        System.out.println(group_count);
        sc.close();
    }

    public static int chk_group_word(String str) {
        char temp = ' ';
        int[] alph_chk = new int[26];
        for (int i=0;i<alph_chk.length;i++) {
            alph_chk[i]=1;
        }

        for(int i=0;i<str.length();i++){
            if(temp != str.charAt(i)){
                temp = str.charAt(i);
                if(alph_chk[str.charAt(i)-97]!=0){
                    alph_chk[str.charAt(i)-97]=0;
                } else {
                    return 0;
                }
            }
        }
        return 1;
    }
}
