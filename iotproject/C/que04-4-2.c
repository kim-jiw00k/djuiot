#include <stdio.h>

int main()
{
	int num1 = 3;

	num1 = num1<<3; //8의 곱  << 비트의 열을 왼쪽으로 한칸씩 옮길때 마다 정수의 값은 두배가 된다.
	num1 = num1>>2; //4의 제  >> 비트의 열을 오른쪽으로 한칸씩 옮길때 마다 정수의 값은 2로 나누어 진다.

	printf("3X8/4의 출력값은 %d 이다. \n ", num1);

	return 0;
}
