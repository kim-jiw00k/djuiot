#include <stdio.h>

int main()
{
	int num = 0;
	int i = 0;
	double avg = 0;
	double point1 = 0;
	double point = 0;

	printf("몇 개의 정수를 입력 할 것인가요? : ");
	scanf("%d", &num);

	while(i < num)
	{
		printf("점수를 입력하시오. : ");
		scanf("%lf", &point);
		point1 += point;
		++i;
	}
	avg = point1 / num;
	printf("평균값은 %lf 이다. \n", avg);

	return 0;
}
