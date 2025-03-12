#include <stdio.h>

int main()
{
	int num = 0;

	while(num < 5)
	{
		printf("Hello world ! %d \n", num);
		num++; // num = num + 1 ; 이게 다른언어에서도 쓰이기 때문에 이게 더 정석
	}

	return 0;
}
