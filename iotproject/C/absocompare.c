#include <stdio.h>
int absocom(int, int);	//절대값이 큰 정수 반환
int getabsovalue(int);	//전달인자의 절대값을 반환

int main()
{
	int num1 = 0;
	int num2 = 0;
	printf("두 개의 정수 입력 : ");
	scanf("%d %d", &num1, &num2);
	printf("%d와 %d중 절대값이 큰 정수 : %d \n", num1, num2, absocom(num1,num2));
	return 0;
}

int absocom(int num1, int num2)
{
	if(getabsovalue(num1) > getabsovalue(num2))
	{
		return num1;
	}
	else
	{
		return num2;
	}
}

int getabsovalue(int num)
{
	if(num<0)
	{
		return num * (-1);
	}
	else
	{
		return num;
	}
}
