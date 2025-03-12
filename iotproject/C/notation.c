#include <stdio.h>

int main()
{
	int num1 = 0xB6;
	int num2 = 0x56;
	int num3 = 025;
	int num4 = 056;

	printf("0xB6의 10진수 정수 값 : %d \n", num1);
	printf("0x56의 10진수 정수 값 : %d \n", num2);
	printf("025의 10진수 정수 값 : %d \n", num3);
	printf("056의 10진수 정수 값 : %d \n", num4);

	printf("%d - %d = %d \n", num1, num2, num1-num2);
	printf("%d + %d = %d \n", num3, num4, num3+num4);

	return 0;
}
