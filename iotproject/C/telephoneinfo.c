#include <stdio.h>
#include <string.h>

struct Person
{
	char name[20];
	char phonenumber[20];
	int age;
};

int main()
{
	struct Person man1 = {'\0' ,'\0' ,0};
	struct Person man2 = {'\0' ,'\0' ,0};
	strcpy(man1.name, "안성준");
	strcpy(man1.phonenumber, "010-1234-5678");
	man1.age = 23;
	printf("이름 입력 : ");
	fgets(man2.name ,sizeof(man2.name) ,stdin);
	printf("번호 입력 : ");
	fgets(man2.phonenumber,sizeof(man2.phonenumber) ,stdin);
	printf("나이 입력 : ");
	scanf("%d", &(man2.age));

	printf("이름 : %s \n", man1.name);
	printf("번호 : %s \n", man1.phonenumber);
	printf("나이 : %d \n", man1.age);

	printf("이름 : %s", man2.name);
	printf("번호 : %s", man2.phonenumber);
	printf("나이 : %d \n", man2.age);

	return 0;
}
