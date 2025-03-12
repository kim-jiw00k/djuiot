#include <stdio.h>

int main(int argc, const char* argv[])
{
	int value = 10000;
	int* ptr = &value;
	int** p_ptr = NULL;
	p_ptr = &ptr;
	**p_ptr = 10;  //두번 가라.
	printf("%d \n", value);
	return 0;
}
