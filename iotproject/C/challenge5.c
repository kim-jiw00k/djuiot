#include <stdio.h>
void prime(int);

int main()
{
	prime(10);
	return 0;
}

void prime(int count)
{
	int num = 2;
	int found = 0;
	while(found < count)
	{
		int is_prime = 1;
		for(int i = 2; i < num; ++i)
		{
			if (num % i == 0)
			{
				is_prime = 0;
				break;	
			}
		}

		if(is_prime)
		{
			printf("%d ", num);
			++found;
		}
		++num;
	}
	printf("\n");
}

