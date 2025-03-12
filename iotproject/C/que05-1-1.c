#include <stdio.h>

int main()
{
	int lx = 0;
	int ly = 0;
	int rx = 0;
	int ry = 0;

	printf("좌 상단x,y의 좌표 :");
	scanf("%d,%d", &lx, &ly);
	printf("우 하단x,y의 좌표 :");
	scanf("%d,%d", &rx, &ry);

	printf("두 점이 이루는 직사각형의 넓이는 %d입니다.\n", (lx-rx)*(ly-ry));
	
	return 0;
}
