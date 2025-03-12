#include <stdio.h>

int main()
{
	int result = 0;
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;

	printf("세 개의 정수 입력 :");
	scanf("%d/%d/%d", &num1, &num2, &num3);

	result = num1 * num2 + num3;
	printf("%d X %d + %d = %d\n", num1, num2, num3, result);

	return 0;
}
