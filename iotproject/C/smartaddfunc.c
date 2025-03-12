#include <stdio.h>

int add(int ,int); //함수의 원형
int showresult(int); //함수의 원형
int read();
int show();

int main()
{
	int result = 0;
	int	num1 = 0;
    int num2 = 0;
	show();
	num1 = read();
	num2 = read();
	result = add(num1, num2);
	showresult(result);

	return 0;
}
int add(int num1, int num2)
{
	return num1+num2;
}
int showresult(int num)
{
	printf("덧셈결과 출력 : %d \n", num);
}
int read()
{
	int num;
	scanf("%d", &num);
	return num;
}
int show()
{
	printf("두 개의 정수를 입력 하시면 덧셈결과가 출력됩니다. \n");
	printf("자! 그럼 두 개의 정수를 입력 하세요. \n");
}
