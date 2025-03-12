#include <stdio.h>

int main()
{
	double rad = 0;
	double area = 0;

	printf("원의 반지름 입력 :");
	scanf("%lf", &rad);

	area = rad*rad*3.1415;
	printf("%lf \n", area);

	return 0;
}
