#include <stdio.h>

int main()
{
	double num = 3.14;
	double* ptr = &num;
	double** dptr = &ptr;
	double* ptr2 = 0;

	printf("%9p %9p \n", ptr, *dptr);
	printf("%9g %9g \n", num, **dptr);
	ptr2 = *dptr;	//ptr2 = ptr 과 같은 문장
	*ptr2 = 10.99;
	printf("%9g %9g \n", num, **dptr);

	return 0;
}
