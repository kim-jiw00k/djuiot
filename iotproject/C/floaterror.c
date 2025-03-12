#include <stdio.h>

int main()
{
	int i = 0;
	float num = 0.0;

	for(i = 0; i < 100; i++)
		num += 0.1; // 이 연산을 총 100회 진행 한다.
	
	printf("0.1을 100번 더한 결과 : %f \n", num);

	return 0;
}
