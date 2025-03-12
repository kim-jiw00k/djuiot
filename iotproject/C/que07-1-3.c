#include <stdio.h>

int main()
{
	int i = 1;
	int num = 0;
	int sum = 0;

	while(i>0)
	{
		printf("정수를 입력하시오.(0을 입력하면 합이 나옵니다.) : ");
		scanf("%d", &i);
		num += i;
	}
	printf("나온 정수의 합은 %d 이다. \n", num);
	return 0;
}
