#include <stdio.h>

void chage(int);

int main()
{
	int sec = 0;
	printf("바꿀 초(second)를 입력 하시오. : ");
	scanf("%d", &sec);

	chage(sec);

	return 0;
}

void chage(int t)
{
	int h = t / 3600;
	int m = (t % 3600) / 60;
	int s = t % 60;
	printf("[%d 시 %d 분 %d 초] 이다. \n", h, m, s);

}
