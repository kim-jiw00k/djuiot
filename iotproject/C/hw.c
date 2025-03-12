#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main()
{
	for(unsigned int degree = 0u; degree <= 360; degree += 5)
	{
		const double sine_value = (double)sin((M_PI / 180.0) * degree);
		/*
		 * 센터를 맞춘다. 100칸 미리 가진다.
		 */
		for(unsigned int count = 0u; count < 50; ++count)
		{
			printf("%s", " ");//100 lines
		}
		if(sine_value > 0)
		{
			int count = (int)(sine_value * 25);
			for(unsigned int i = 0u; i < count; ++i)
			{
				printf("%s", " ");
			}
			printf("%s", "*");
		}
		else if(sine_value < 0 )
		{
			int count = (int)(sine_value * 25);
			for(unsigned int i = 0u; i< -count; ++i)
			{
				printf("%s", "\b");
			}
			printf("%s", "*");
		}
		else
		{
			printf("%s", "*");
		}
		printf("%s", "\r\n");
	}
	return 0;
}
