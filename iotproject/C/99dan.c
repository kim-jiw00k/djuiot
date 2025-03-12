#include <stdio.h>

int main()
{
	int dan = 0;
	int num = 1;
	printf("몇 단? ");
	scanf("%d", &dan);

	while(num <10)
	{
		printf("%d X %d = %d \n", dan, num, dan*num);
		num = num + 1;
	}
	return 0;
}
