#include <stdio.h>
void gcd(int,int);

int main()
{
	int num1 = 0;
	int num2 = 0;
	printf("두 개의 정수 입력 : ");
	scanf("%d %d", &num1, &num2);
	gcd(num1,num2);

	return 0;
}

void gcd(int n1,int n2)
{
	if (n1 < n2)	// n1이 n2 보다 작을 때
	{
		for(int i = n1; i>=1; --i) // 작은 값부터 1까지 검사
		{
			if(n1 % i == 0 && n2 % i == 0) // 둘 다 나머지가 0 이면 출력
			{
				printf("두 수의 최대 공약수 : %d \n", i);
				return; // 최대 공약수 찾고 종료
			}
		}
	}
	else (n1 > n2); // n2가 n1보다 작을 때
	{
		for (int i = n2; i >= 1; --i)

			if(n1 % i == 0 &&  n2 % i == 0)
			{
				printf("두 수의 최대 공약수 : %d \n", i);
				return;
			}
		}
	}
