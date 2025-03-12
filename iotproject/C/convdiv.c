#include <stdio.h>

int main()
{
	int num1 = 3;
	int num2 = 4;
	double divResult = 0;
	divResult = (double)num1 / (double)num2; //명시적 형변환을 해줘야 원하는답이 나온다.
	//divResult = (double)num1 / num2;도 가능하다.
	printf("나눗셈 결과 : %f \n", divResult);

	return 0;
}
