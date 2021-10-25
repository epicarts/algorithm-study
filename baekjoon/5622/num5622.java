package part_stringarray;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class num5622 {
    public static void main(String[] args) {
        Map<Integer,Object> m1 = new HashMap<Integer,Object>();
        ArrayList<String> arr = new ArrayList<String>();
        int asc = 65;
        int num = 0;
        for(int i=2;i<10;i++){
            for(int j=0;j<3;j++){
                arr.add(Integer.toString(asc++));
            }
            if(i==7 || i==9){
                arr.add(Integer.toString(asc++));
            }
            m1.put(i, arr);
            arr = new ArrayList<String>();
        }
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        for (int i = 0; i < s.length(); i++) {
            num = num + searchAlph(s.charAt(i),m1)+1;
        }
        System.out.println(num);
        sc.close();
    }

    public static int searchAlph(char a,Map<Integer,Object> m){
        ArrayList<String> arr = new ArrayList<String>();
        for(int i=2;i<m.size()+2;i++){
            arr = (ArrayList<String>) m.get(i);
            for (String str : arr) {
                if(Integer.parseInt(str) == (int)a){
                    return i;
                }
            }
        }
        return 0;
    }
}
