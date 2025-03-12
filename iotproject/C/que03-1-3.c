#include <stdio.h>

int main()
{
	int result = 0;
	int num1 = 0;

	printf("하나의 정수를 입력하시오. :");
	scanf("%d", &num1);

	result = num1 * num1;
	printf("입력된 정수는 %d 이며  제곱은 %d 이다.\n", num1, result);

	return 0;
}
