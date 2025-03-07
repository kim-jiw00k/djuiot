#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct ListNode
{
	struct ListNode* llink;
	char data[4];
	struct ListNode* rlink;
}lN;

typedef struct
{
	lN* head;
}ll_h;

ll_h* createll(void);
void print(ll_h* DL);
void insert(ll_h* DL, lN* pre, char* x);
void delete(ll_h* DL, lN* old);
lN* search(ll_h* DL, char* x);

int main()
{
	ll_h* DL;
	lN* p;
	
	DL = createll();
	printf("(1) 이중 연결 리스트 생성하기 ! \n");
	print(DL);

	printf("(2) 이중 연결 리스트에 [월] 노드 삽입하기 ! \n");
	insert(DL,NULL,"월");
	print(DL);

	printf("(3) 이중 연결 리스트에 [월] 노드 뒤에 [수] 노드 삽입하기 ! \n");
	p = search(DL,"월");
	insert(DL,p,"수");
	print(DL);	
	
	printf("(4) 이중 연결 리스트에 [수] 노드 뒤에 [금] 노드 삽입하기 ! \n");
	p = search(DL,"수");
	insert(DL,p,"금");
	print(DL);	

	printf("(5) 이중 연결 리스트에 [수] 노드 삭제하기 ! \n");
	p = search(DL,"수");
	delete(DL,p);
	print(DL);

	getchar();
	return 0;
}

ll_h* createll(void)
{
	ll_h* DL;
	DL = (ll_h*)malloc(sizeof(ll_h));
	DL -> head = NULL;
	return DL;
}

void print(ll_h* DL)
{
	lN* p;
	printf(" DL = (");

	p = DL -> head;
	while(p != NULL)
	{
		printf("%s", p -> data);
		p = p -> rlink;
		if(p != NULL) printf(", ");
	}
	printf(") \n");
}

void insert(ll_h* DL, lN* pre, char* x)
{
	lN* new;
	new = (lN*)malloc(sizeof(lN));
	strcpy(new -> data, x);
	if(DL -> head == NULL)
	{
		new -> rlink = NULL;
		new -> llink = NULL;
		DL -> head = new;
	}
	else
	{
		new -> rlink = pre -> rlink;
		pre -> rlink = new;
		new -> llink = pre;
		if(new -> rlink != NULL)
		{
			new -> rlink -> llink = new;
		}
	}
}

void delete(ll_h* DL, lN* old)
{
	if(DL -> head = NULL) return;
	else if(old == NULL) return;
	else
	{
		old -> llink -> rlink = old -> rlink;
		old -> rlink -> llink = old -> llink;
		free(old);
	}
}

lN* search(ll_h* DL, char* x)
{
	lN* temp;
	temp = DL -> head;
	while (temp != NULL)
	{
		if(strcmp(temp -> data, x) == 0) return temp;
		else temp = temp -> rlink;
	}
	return temp;
}
