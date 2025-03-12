#include <stdio.h>

int add(int,int);
void function_add(int (*)(int,int));

int main(int argc, const char* argv[])
{
	int (*f_ptr)(int,int) = NULL;
	f_ptr = add;
	int result1 = add(10 ,20);
	int result2 = f_ptr(10,20);
	printf("%d \n", result1);
	printf("%d \n", result2);
	function_add(add); // or function_add(f_ptr);
	f_ptr = NULL;
	return 0;
}

int add(int number1, int number2)
{
	return number1+number2;
}

void function_add(int (*f_param)(int,int))
{
	puts("Call back 호출");
	f_param(10,20);
}
