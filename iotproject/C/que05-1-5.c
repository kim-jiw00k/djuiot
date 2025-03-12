#include <stdio.h>

int main()
{
	char ch1 = 0;

	printf("알파벳 문자 하나를 입력하시오. : ");
	scanf("%c", &ch1);
	printf("입력한 알파벳의 아스키 코드는 %d이다. \n", ch1);

	return 0;
}
