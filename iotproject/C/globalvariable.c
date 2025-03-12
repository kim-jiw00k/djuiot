#include <stdio.h>
static void add(int);
int num = 0;

int main()
{
	printf("num : %d \n", num);
	add(3);
	printf("num : %d \n", num);
	num++;
	printf("num : %d \n", num);
	return 0;
}

void add(int val)
{
	num += val; //전역변수 num의 값 val 만큼 증가
}
