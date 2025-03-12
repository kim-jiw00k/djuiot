#include <stdio.h>

struct Point
{
	int xpos;
	int ypos;
};

int main()
{
	struct Point pos1 = {1, 2};
	struct Point pos2 = {100, 200};
	struct Point* pptr = &pos1;

	(*pptr).xpos += 4;
	(*pptr).ypos += 5;
	printf("[%d, %d] \n", pptr->xpos, pptr->ypos);

	pptr = &pos2;
	pptr -> xpos += 1;
	pptr -> ypos += 2;
	printf("[%d, %d] \n", (*pptr).xpos, (*pptr).ypos);
	return 0;
}
