#include <stdio.h>
static void simplefuc();

int main()
{
	for(int i = 0; i < 3; ++i)
	{
		simplefuc();
	}
	return 0;
}

void simplefuc()
{
	static int num1 = 0;
	int num2 = 0;
	++num1;
	++num2;
	printf("static : %d, local : %d \n", num1, num2);
}
