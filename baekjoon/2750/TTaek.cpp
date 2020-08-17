#include<iostream>
using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* arr = new int[n];
	
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	int tmp;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n - 1 - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		cout << arr[i] << endl;
	}

	return 0;
}