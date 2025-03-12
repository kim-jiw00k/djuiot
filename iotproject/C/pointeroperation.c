#include <stdio.h>

int main()
{
	int num1 = 100;
	int num2 = 100;
	int* ptr_num = NULL;

	ptr_num = &num1;		//포인터 pnum이 num1을 가리킴
	(*ptr_num) += 30;		//num1 += 30; 이랑 동일
	
	ptr_num = &num2;		//포인터 pnum이 num2을 가리킴
	(*ptr_num) -= 30;		//num2 -= 30; 이랑 동일
	
	printf("num1 : %d\nnum2 : %d \n", num1, num2);
	return 0;
}
