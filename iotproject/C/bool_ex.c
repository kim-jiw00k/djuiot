#include <stdio.h>
#include <stdbool.h>

int main()
{
	bool isState = true; //true , false
	fprintf(stdout, "%b\r\n", isState);
	printf("%s\r\n",  isState ? "true":"false");

	return 0;
}
