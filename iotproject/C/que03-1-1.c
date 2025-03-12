#include <stdio.h>

int main()
{
	int result1 = 0; // 뺄셈 값
	int result2 = 0; // 곱셈 값
	int num1 = 0;
	int num2 = 0;

	printf("두 개의 정수 입력 :");
	scanf("%d/%d", &num1, &num2);

	result1 = num1 - num2;
	result2 = num1 * num2;
	printf("%d - %d = %d\n", num1, num2, result1);
	printf("%d * %d = %d\n", num1, num2, result2);

	return 0 ;
}
