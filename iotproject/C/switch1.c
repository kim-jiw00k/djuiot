#include <stdio.h>

void swap();

int a = 10;
int b = 20;

int main()
{
	printf("원래 값 : %d %d \n", a, b);
	swap();

	return 0;
}

void swap()
{
	int temp = a;
	a = b;			 //a -> 20
	b = temp;		// b -> 10
	printf("바뀐 값 : %d %d \n", a, b);
}
