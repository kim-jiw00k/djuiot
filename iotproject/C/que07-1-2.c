#include <stdio.h>

int main()
{
	unsigned int num = 1;
	int i = 1;
	
	printf("양의 정수를 입력 하시오. : ");
	scanf("%d", &num);

	while(i < num+1)
	{
		printf("%d \n", i*3);
		++i;
	}
	return 0;
}
