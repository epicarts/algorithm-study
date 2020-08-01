# 문제 주소
https://chldudgh.com

## 문제 접근 방법
- 문제 접근 방법...

### 코드
```java
import java.util.Scanner;
public class Baekjoon1912 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i=0;i<n;i++){
            arr[i]=scanner.nextInt();
        }
        System.out.println(solution(n, arr));
    }
    private static int solution(int n, int[] arr) {
        int[] dp = new int[n];
        dp[0]=arr[0];
        for (int i=1;i<n;i++){
            dp[i]=Math.max(dp[i-1]+arr[i], arr[i]);
        }
        int max=Integer.MIN_VALUE;
        for (int i:dp){
            if (max<i) max=i;
        }
Comment on lines +35 to +38
 @OHHAKO
OHHAKO on 23 Jun Member
푼제풀이 확인 했습니다:) 고생하셨어요! 프로그램의 첫번째 코드에 max 연산을 넣으면 최대값을 찾는 반복문을 수행하지 않을 수 있어요. 이미 알고 계실거라 생각하지만...ㅎㅎ
추가적으로 이 코드에서
MIN_VALUE는 숫자 클래스의 최소값 상수인데 0이 아닌 최소값 상수를 할당한 이유가 무엇인지 궁금해요!
@epicarts	Reply…
        return max;
    }
}
```
### Time complexity
O(n)
### Space complexity
O(n)