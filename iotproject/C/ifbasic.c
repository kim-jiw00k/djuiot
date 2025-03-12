#include <stdio.h>

int main()
{
	int num = 0;
	printf("정수입력 : ");
	scanf("%d", &num);

	if(num < 0)
	{
		printf("입력 값은 0 보다 작다. \n");
	}
	if(num > 0)
	{
		printf("입력 값은 0 보다 크다. \n");
	}
	if(num == 0)
	{
		printf("입력 값은 0 이다. \n");
	}

	return 0;
}
