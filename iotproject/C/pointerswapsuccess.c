#include <stdio.h>

void swap(int**,int**);

int main()
{
	int num1 = 10;
	int num2 = 20;
	int *ptr1 = &num1;
	int *ptr2 = &num2;
	printf("*ptr1 , *ptr2 : %d %d \n", *ptr1, *ptr2);

	swap(&ptr1,&ptr2);
	printf("*ptr1 , *ptr2 : %d %d \n", *ptr1, *ptr2);
	return 0;
}

void swap(int**dp1, int **dp2)
{
	int *temp = *dp1;
	*dp1 = *dp2;
	*dp2 = temp;
}
