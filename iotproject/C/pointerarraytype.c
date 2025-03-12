#include <stdio.h>

int main()
{
	int num1 = 10;
	int num2 = 20;
	int num3 = 30;
	int *ptr1 = &num1;
	int *ptr2 = &num2;
	int *ptr3 = &num3;

	int* ptrarr[]={ptr1, ptr2, ptr3};
	int** dptr=ptrarr;

	printf("%d %d %d \n", *(ptrarr[0]), *(ptrarr[1]), *(ptrarr[2]));
	printf("%d %d %d \n", *(dptr[0]), *(dptr[1]), *(dptr[2]));

	return 0;
}
