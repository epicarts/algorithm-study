#include <iostream>
using namespace std;

int main()
{
	int arr[5];
	int bug, dri = 2001, temp = 0;

	for (int i = 0; i < 3; i++)
	{
		cin >> arr[i];

		if (i == 0)
		{
			bug = arr[0];
		}

		else if (0 < i < 3)
		{
			if (arr[i] < bug)
			{
				bug = arr[i];
			}
		}
	}

	for (int i = 3; i < 5; i++)
	{
		cin >> arr[i];
		if (arr[i] < dri)
			dri = arr[i];
	}

	temp = bug + dri - 50;
	cout << temp;

	return 0;
}