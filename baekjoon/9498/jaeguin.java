import java.util.Scanner;

public class main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();

        if(i>= 90 && i <= 100) System.out.print("A");
        else if(i>= 80 && i <= 89) System.out.print("B");
        else if(i>= 70 && i <= 79) System.out.print("C");
        else if(i>= 60 && i <= 69) System.out.print("D");
        else System.out.print("F");

    }

}
