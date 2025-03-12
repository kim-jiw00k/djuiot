#include <stdio.h>

int main()
{
	unsigned int positive = 0u;
	unsigned int negative = 0u;
	unsigned int zero = 0u;
	for(int count = 0; count < 5; ++count)
	{
		int input_number = 0;
		puts("숫자 입력");
		scanf("%d", &input_number);
		if(input_number > 0)
		{
			++positive;
		}
		else
		{
			if(input_number == 0)
			{
				++zero;
			}
			else
			{
				++negative;
			}
		}
	}
	printf("양수는 %d 음수는 %d 0은 %d \n", positive, negative, zero);
	return 0;
}
