#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int a=0;
	cin >> a;
	int arr[1000];

	for (int i = 0; i < a; i++)
	{
		cin >> arr[i];
	}

	sort(arr, arr + a);

	int cnt = 0;
	for (int j = 0; j < a; j++)
	{
		int tmp = 0;
		for (int k = 0; k <= j; k++)
		{
			tmp += arr[k];
		}
		cnt += tmp;
	}
	cout << cnt << endl;

	return 0;
}