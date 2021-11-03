package part_dynamic;

import java.util.Scanner;

public class num1463 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        
        int[] arr = new int[num+1];
        
        arr[0]=0;
        arr[1]=0;
        
        for(int i=2;i<=num;i++){
            arr[i] = arr[i-1]+1;
            if(i%2==0) arr[i] = Math.min(arr[i],arr[i/2]+1);
            if(i%3==0) arr[i] = Math.min(arr[i],arr[i/3]+1);
        }
        System.out.println(arr[num]);
        sc.close();
    }

}
