#include <stdio.h>

void ninety(int(*goo)[4]);
void baekpal(int(*)[4]);
void yeebaek(int(*)[4]);

int main()
{
	int	arr[4][4] =	{
			{1,2,3,4},
			{5,6,7,8},
			{9,10,11,12},
			{13,14,15,16}
		};
	printf("90도 돌렸을때\n");
	ninety(arr);
	printf("180도 돌렸을때 \n");
	baekpal(arr);
	printf("270도 돌렸을때 \n");
	yeebaek(arr);

	return 0;
}

void ninety(int(*goo)[4])
{
	int i = 0;
	int j = 0;
	int goosip[4][4];
	//90도 돌리는 함수
	for(i = 0; i < 4; ++i)
	{
		for(j = 0; j < 4; ++j)
		{
			goosip[j][3-i] = goo[i][j];
		}
	}
	//원본 배열에 회전된 배열을 복사
	for(i = 0; i < 4; ++i)
	{
		for(j = 0; j < 4; ++j)
		{
			goo[i][j] = goosip[i][j];
		}
	}
	// 출력 하는 문
	for(i = 0; i < 4; ++i)
	{
		for(j = 0; j < 4; ++j)
		{
			printf("%d \t", goosip[i][j]);
		}
	printf("\n");
	}
}
void baekpal(int (*goo)[4])
{
	ninety(goo);
}

void yeebaek(int (*goo)[4])
{
	ninety(goo);
}
