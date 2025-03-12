#include <stdio.h>

void swap(int*,int*);

int main()
{
	int num1 = 10;
	int num2 = 20;
	int* ptr1 = 0;
	int* ptr2 = 0;
	ptr1 = &num1;
	ptr2 = &num2;

	printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);

	swap(ptr1,ptr2);
	printf("*ptr1, *ptr2 : %d %d \n", *ptr1, *ptr2);

	return 0;
}

void swap(int* p1,int* p2)
{
	int* temp = p1;
	p1 = p2;
	p2 = temp;
}
