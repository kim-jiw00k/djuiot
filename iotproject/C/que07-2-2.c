#include <stdio.h>

int main()
{
	int circle = 0;
	int line = 0;

	while(line < 5)
	{
		circle = 0;
		while(circle < line)
		{
			printf("0");
			circle++;
		}
		printf("*\n");
		line++;
	}
	return 0;
}
