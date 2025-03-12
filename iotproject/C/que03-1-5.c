#include <stdio.h>

int main()
{
	int result = 0;
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;

	printf("세 개의 정수를 입력하시오. :");
	scanf("%d/%d/%d", &num1, &num2, &num3);

	result=(num1-num2)*(num2+num3)*(num3%num1);
	printf("연산 결과는 %d 이다.\n", result);

	return 0;
}
