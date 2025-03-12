#include <stdio.h>

int main()
{
	int num1 = 0;

	printf("정수를 입력 하시오. :");
	scanf("%d", &num1);
	num1 = ~num1;
	num1 = num1 + 1;
	printf("반전된 부호의 정수 값 : %d \n", num1);

	return 0;
}
