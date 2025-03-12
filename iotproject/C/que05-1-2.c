#include <stdio.h>

int main()
{
	double num1 = 0;
	double num2 = 0;

	printf("두개의 실수를 입력 하시오.");
	scanf("%lf,%lf", &num1, &num2);

	printf("두 실수의 사칙연산은 \n 합 : %lf \n 차 : %lf \n 곱 : %lf \n 나누기 : %lf \n", num1+num2, num1-num2, num1*num2, num1/num2);

	return 0;
}
