#include <stdio.h>

int add(int);
int num = 1;

int main()
{
	int num = 5;
	printf("num : %d \n", add(3));
	printf("num : %d \n", num + 9);
	return 0;
}

int add(int val)
{
	int num = 9;
	num += val;
	return num;
}
