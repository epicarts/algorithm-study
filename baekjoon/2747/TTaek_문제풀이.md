# 문제 주소
https://www.acmicpc.net/problem/2747

## 문제 접근 방법
피보나치 수열 - 배열사용

### 코드
```cpp
#include <iostream>
using namespace std;

int A(int n){
	int arr[3] = { 0,1,1 };
	for (int i = 2; i < n; i++) {
		arr[(i + 1) % 3] = arr[i % 3] + arr[(i - 1) % 3];
	}
	return arr[n % 3];
}

int main(void) {

	int num;
	cin >> num;
	cout << A(num);

	return 0;
}
```