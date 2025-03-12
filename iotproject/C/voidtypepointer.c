#include <stdio.h>

void sosimplefunc();

int main()
{
	int num = 20;
	void* ptr;

	ptr = &num;
	printf("%p \n", ptr);

	ptr=sosimplefunc;
	printf("%p \n", ptr);

	return 0;
}

void sosimplefunc()
{
	printf("I'm So Simple");
}
