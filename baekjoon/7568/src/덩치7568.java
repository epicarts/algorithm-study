import java.util.Scanner;

public class 덩치7568 {
    public static void main(String[] args){

        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int[][] arr = new int[N][2];

        for(int i = 0; i < N; i++) {
            arr[i][0] = in.nextInt();	// [i][0] : 몸무게
            arr[i][1] = in.nextInt();	// [i][1] : 키
        }


        for(int i = 0; i < N; i++) {
            int rank = 1;

            for(int k = 0; k < N; k++) {
                if(i == k) continue;
                if (arr[i][0] < arr[k][0] && arr[i][1] < arr[k][1]) {
                    rank++;
                }
            }

            System.out.print(rank + " ");
        }

    }
}