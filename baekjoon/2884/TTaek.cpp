#include <iostream>
using namespace std;

int main()
{
	int h = 0;
	int m = 0;

	cin >> h >> m;

	if ((m - 45) < 0)
	{
		h = h - 1;
		if (h < 0)
		{
			h = 23;
			cout << h << " " << (m - 45) + 60 << endl;
		}

		else
		{
			cout << h << " " << (m - 45) + 60 << endl;
		}
	}
	else
	{
		cout << h << " " << m - 45 << endl;
	}

	return 0;
}