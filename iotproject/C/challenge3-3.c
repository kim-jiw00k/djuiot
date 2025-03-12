#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i = 0;
	
	printf("난수의 범위 : 0 부터 %d 까지 \n", RAND_MAX % 1073741774);
	for(i=0;i<5;++i)
	{
		printf("난수 출력 : %d \n",rand()%100);
	}
	return 0;
}
