#include <stdio.h>

int main()
{
	int mean = 0;
	int i = 0;
	int j = 0;
	int record[3][3][2] ={
		{	
			{70, 80},
			{94, 90},
			{70, 85}
		},
		{
			{83, 90},
			{95, 60},
			{90, 82}
		},
		{
			{98,89},
			{99,94},
			{91,87}
		}
	};

	for(i = 0; i < 3; ++i)
	{
		for(j = 0; j < 2; ++j)
		{
			mean += record[0][i][j];
		}
	}
	printf("A 학급 전체 평균 : %g \n", (double)mean/6);
	
	mean = 0;
	for(i = 0; i < 3; ++i)
	{
		for(j = 0; j < 2; ++j)
		{
			mean += record[1][i][j];
		}
	}
	printf("B 학급 전체 평균 : %g \n", (double)mean/6);
	
	mean = 0;
	for(i = 0; i < 3; ++i)
	{
		for(j = 0; j < 2; ++j)
		{
			mean += record[2][i][j];
		}
	}
	printf("C 학습 전체 평균 : %g \n", (double)mean/6);

	return 0;
}
