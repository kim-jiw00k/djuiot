#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Employee
{
	char name[20];		//이름
	char idnum[20];		//주민번호
	int pay;			//급여정보
};

int main()
{
	struct Employee man = {'\0','\0',0};	//구조체 변수 선언 및 초기화
	printf("이름 입력 : ");
	fgets(man.name, sizeof(man.name), stdin);
	printf("주민 번호 : ");
	fgets(man.idnum, sizeof(man.idnum), stdin);
	printf("급여 정보 : ");
	scanf("%d", &man.pay);

	printf("이름 : %s", man.name);
	printf("주민 번호 : %s", man.idnum);
	printf("급여 정보 : %d \n", man.pay);

	return 0;
}
