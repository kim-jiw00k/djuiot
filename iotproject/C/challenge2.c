#include <stdio.h>
void googoo(int,int); // 인자는 전달 되지만 반환값이 없음.

int main()
{
	int num1 = 0;
	int num2 = 0;
	printf("두 개의 정수를 입력하시오. :");
	scanf("%d,%d", &num1, &num2);
	googoo(num1, num2);
	return 0;
}

void googoo(int dan1,int dan2)
{
	if (dan1>dan2)
	{
		for(int j = dan2; j <= dan1; ++j)
		{
			for (int i = 1; i < 10; ++i)
			{
				printf("%d X %d = %d \n", j, i, j*i);
			}
		}
	}
	else
	{
		for(int j = dan1; j <= dan2; ++j)
		{
			for (int i = 1; i < 10; ++i)
			{
				printf("%d X %d = %d \n", j , i, j*i);
			}
		}
	}
}
