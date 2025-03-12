#include <stdio.h>

int main()
{
	char ch = 9;
	int n_Num = 1052;
	double d_Num = 3.1415;

	printf("변수 ch의 크기 : %lu \n", sizeof(ch));
	printf("변수 n_Num의 크기 : %lu \n", sizeof n_Num);
	printf("변수 d_Num의 크기 : %lu \n", sizeof d_Num);

	printf("char의 크기 : %lu \n", sizeof(char));
	printf("int의 크기 : %lu \n", sizeof(int));
	printf("long의 크기 : %lu \n", sizeof(long));
	printf("long long의 크기 : %lu \n",sizeof(long long));
	printf("float의 크기 : %lu \n", sizeof(float));
	printf("double의 크기 : %lu \n", sizeof(double));
/*크기를 알려줘야 하므로 음수가 나올 수 없다.
 * 그리하여 %d는 맞지 않을 수가 있으며 unsigned 가 필요하여 %d 보단 %u가 맞으며
 * 수가 클 수도 있기에 long을 붙여 %lu로 하면 컴파일이 된다.
 * lu = long unsigned*/
	return 0;
}
