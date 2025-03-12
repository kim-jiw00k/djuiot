#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	srand((int)time(NULL));
	int i = 0;
	int r = rand()%45 + 1;

	printf("로또 출력 1~45 까지\n");
	for(i = 0; i<5; i++)
	{
		printf("%d ", r);
	}
	printf("\n");

	return 0;
}
