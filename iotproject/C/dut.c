#include <stdio.h>

void adder(int,int);

int main()
{
	void (*ptr_sum)(int,int) = adder;
	ptr_sum(3,4);
	return 0;
}


void adder(int n1, int n2)
{
	printf("%d + %d = %d \n", n1, n2, n1+n2);
}
