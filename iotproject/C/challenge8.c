#include <stdio.h>

int rec(int);

int main()
{
	int num = 0;
	printf("정수 입력 : ");
	scanf("%d", &num);
	printf("2의 %d 승은 %d 이다. \n", num, rec(num));

	return 0;
}

int rec(int n)
{
	int result = 0;
	if(n == 0)
	{
		return 1;
	}
	return result = rec(n-1) * 2;
}
