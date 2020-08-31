#include <iostream>
using namespace std;

int main()
{
	int name[5];
	int sum = 0;
	int average = 0;

	for (int i = 0; i < 5; i++)
	{
		cin >> name[i];
	}

	for (int i = 0; i < 5; i++)
	{
		if (name[i] < 40)
		{
			name[i] = 40;
		}

		sum += name[i];
	}

	average = sum / 5;

	cout << average;

	return 0;
}