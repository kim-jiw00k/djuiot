#include <stdio.h>

int main()
{
	int number = 100;
	int* ptr_number = NULL;
	//const int* ptr_number = &number; 이렇게 하면 상수형 포인터로 가능
	ptr_number = &number;
	//*ptr_number; // number;
	*ptr_number = 10000;
	ptr_number = NULL;
	printf("%d \n", number);

	return 0;
}
