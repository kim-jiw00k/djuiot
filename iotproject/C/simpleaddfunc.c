#include <stdio.h>
int add(int, int); //함수의 원형 (proto type)

int main()
{
	int param1 = 30;
	int param2 = 40;
	int result = add(param1,param2);
	return 0;
}

int add(int param1, int param2)
{
	return param1 + param2;
}
