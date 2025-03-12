#include <stdio.h>

void swap(int,int);

int main()
{
	int a = 2;
	int b = 3;
	printf("원래 값은 %d , %d 이다.\n", a, b);
	swap(a,b);
	return 0;
}

void swap(int n, int num)
{
	int s = n;	//잠깐 n의 값이 들어가야해서 만든 s
	n = num;	//num값이 n으로 들어감. n값 에 num 값이 들어감
	num = s;	//원래 n 값이 s로 들어가서 num 에 s가 들어감
	printf("변한 값은 %d , %d 이다.\n", n, num);
}
