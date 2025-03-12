#include <stdio.h>

int main()
{
	int result1 = 0;
	int result2 = 0;
	int num1 = 0;
	int num2 = 0;

	printf("두 개의 정수를 입력하시오 :");
	scanf("%d/%d", &num1, &num2);

	result1= num1 / num2;
	result2= num1 % num2;
	printf("입력된 정수는 %d 와 %d 이며 몫은 %d 이고 나머지는 %d 이다.\n", num1, num2, result1, result2);

	return 0;
}
