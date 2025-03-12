#include <stdio.h>
int bignum(int,int,int); // 가장 큰 수와 작은수를 반환
int smallnum(int,int,int);

int main()
{
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;
	printf("세 개의 정수 입력 : ");
	scanf("%d,%d,%d", &num1, &num2, &num3);
	printf("%d와%d와%d중 가장 큰 수는 %d이고 작은 수는 %d이다. \n", num1, num2, num3, bignum(num1,num2,num3), smallnum(num1, num2, num3));

	return 0;
}

int bignum(int num1, int num2, int num3)
{
	if(num1 > num2 && num1 > num3)
	{
		return num1;
	}
	else if(num2 > num1 && num2 > num3)
	{
		return num2;
	}
	else
	{
		return num3;
	}
}
int smallnum(int num1, int num2, int num3)
{
	if(num1 < num2 && num1 < num3)
	{
		return num1;
	}
	else if(num2 < num1 && num2 < num3)
	{
		return num2;
	}
	else
	{
		return num3;
	}
}
