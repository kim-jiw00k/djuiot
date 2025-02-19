#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void lgin();		 //로그인 동의 함수
void login();		 //로그인 화면 함수
void accetime();	 //본인 확인 및 시간
void screen();		 //초기 화면
void productin();	 //제품 입력
void checkprod();	 //제품 확인
void payment();		 //결제로 이동
void findprod();	 //제품 찾기로 이동
void fin();		 //종료로 이동

//로그인 구조체
struct Loginfo
{
	char id[20];
	char passwd[20];
};

//제품 구조체
struct Product
{
	char prodname[20];		//이름
	char makename[20];		//제조사
	char exp[20];			//유통기한
	int adult;			//성인여부
	int price;			//가격
	int count;			//재고
};

// 전역 변수로 하여 다른 함수들에서도 쓸 수 있게 만듦
struct Loginfo user1 = {'\0', '\0'};    //아이디 비밀번호 받기 여기다가 기본 비밀번호를 입력
struct Loginfo user2 = {'\0', '\0'};    //여기서 아이디와 비밀번호를 입력하고 user1과 틀렸는지 확인
struct Product prod1[50];               //들어 갈 수 있는 제품 수
int prod_count = 0;				//제품을 등록할 곳
int account = 1234000;				//초기 잔고 1,234,000 원
time_t start = 0;				//시작시간 전역변수 선언
time_t end = 0;					//끝날 시간 전역변수 선언
int paytime = 0;				//분 당 시간을 담을 변수

int main()
{
	lgin();			//로그인 동의
	login();		//로그인 화면
	accetime(); 		//본인 확인 및 시간
	time(&start);		//시작 시간
	screen();		//초기 화면,제품 메뉴
	time(&end);		//종료시간
	fin();    //종료 화면
	

	return 0;
}

//로그인 동의
void lgin()							//시작 시 로그인 동의
{
	int access = 0;	
	while(1)						//아니오를 고를경우 무한 되물음
	{
		printf("로그인을 할 것인가요?\n예 : 1\t 아니오 : 2\n");
		scanf("%d", &access);	
		if(access == 1)
		{
			system("clear");			//화면 초기화
			printf("로그인 화면으로 이동 합니다.\n");
			sleep(3);				//3초후 초기화 에서 3초후
			system("clear");			//초기화
			break;					//1고를 경우 무한루프 탈출
		}
		else if(access == 2)
		{
			system("clear");
			printf("로그인을 하지 않습니다.\n");
			sleep(3);
			system("clear");
		}
	}
}
//로그인 화면 함수
void login()
{
	strcpy(user1.passwd, "1234");				//기본 비밀번호 1234를 user1.passwd에 삽입
	while(1)
	{
		printf("ID : ");
		scanf("%s",user1.id);	
		printf("PASSWD (기본 1234) : ");
		scanf("%s",user2.passwd);      			//user2로 비밀번호를 입력 받고
		if(strcmp(user1.passwd, user2.passwd))  	//user1.passwd와 user2.passwd가 맞는지 확인
		{
			printf("비밀번호가 다릅니다.\n");     	 //반환값 0이 아닌 다른 값
		}
		else
		{
			printf("로그인 되었습니다.\n");
			break; 					 //비밀 번호가 맞을 시 탈출 반환값 0
		}
	}
}

//본인 확인
void accetime()
{
	system("clear");
	int acc = 0;		//확인 받을 변수
	printf("사원 %s 본인이 맞습니까? : ", user1.id); 	 //id 가 사원 명과 같음
	scanf("%d", &acc);
	while(1)
	{
		if (acc == 1)
		{
			printf("확인 되었습니다.\n");
			sleep(1);
			system("clear");
			printf("현재 잔고 : %d 원 \n", account);
			sleep(1);
			system("clear");
			break;
		}
		else(acc == 2);
		{
			printf("다시 로그인 합니다.\n");
			login();
			accetime();
			break;
		}
	}
}

//제품 메뉴
void screen()
{
	int num;										// 어디갈지 입력 받음
	printf("1. 제품 입력   2. 제품 확인   3. 제품 입고   4. 계산   5. 제품 찾기   6. 종료\n");	//\t를 쓰니까 4~5번 간격이 이상해져서 억지로 늘림
	scanf("%d", &num);
	if(num == 1)
	{
		printf("제품 입력으로 이동합니다. \n");
		sleep(1);
		system("clear");
		productin();									//제품 입력으로 이동
	}
	else if(num == 2)
	{
		printf("제품 확인으로 이동합니다. \n");
		sleep(1);
		system("clear");
		checkprod();									//제품 확인으로 이동
	}
	else if(num == 3)
	{
		printf("제품 입고로 이동합니다. \n");
		sleep(1);
		system("clear");
		productin();									//제품 입고로 이동
	}
	else if(num == 4)
	{
		printf("계산으로 이동합니다.");
		sleep(1);
		system("clear");
		payment();									//결제로 이동
	}
	else if(num == 5)
	{
		printf("제품 찾기로 이동합니다.\n");
		sleep(1);
		system("clear");
		findprod();									//제품 찾기로 이동
	}
	else if(num == 6)
	{
		printf("오늘의 일당 계산 후 종료 합니다.\n");
		sleep(1);
		system("clear");
		return;										//함수 종료
	}
}

// 제품 입력 메뉴
void productin()
{
	int i = 0;
	while(1)
	{
		if(prod_count >= 50)				//제품의 수 최대치
		{
			printf("더 이상 제품을 추가 할 수 없습니다. \n");
		}
		else
		{
			break;
		}
	}

	struct Product prod = {'\0','\0','\0',0,0,0};		//함수 내에서 쓸 구조체 변수

	printf("1. 제품명 입력 : ");
	scanf("%s", prod.prodname);
	printf("2. 제조회사 입력 : ");
	scanf("%s", prod.makename);
	printf("3. 유통기한 입력 : ");
	scanf("%s", prod.exp);
	printf("4. 19금 물건 확인(1 : 예 , 0 : 아니오) : ");
	scanf("%d", &prod.adult);
	printf("5. 가격 : ");
	scanf("%d", &prod.price);
	prod.count = 1;

	//제품이 존재하는지 확인
	for(i = 0; i < prod_count; ++i)
	{
		if(!strcmp(prod1[i].prodname,prod.prodname))
		{
			prod1[i].count += prod.count;				//이미 존재하는 제품이면 수량 증가
			printf("이미 제품이 있어 재고가 늘어났습니다.\n");
			sleep(3);
			system("clear");
			screen();
		}
	}
		//새 제품은 배열에 추가
		prod1[prod_count] = prod;				//전역변수인 prod1에 지역변수인 prod를 넣는건데 위치는 prod1[0]이다 재고가 늘수록 다음 배열에 들어감
		++prod_count;

	printf("제품이 추가 되었습니다. \n");
	sleep(3);
	system("clear");
	screen();
}

//제품 확인 메뉴
void checkprod()		
{
	int i = 0;
	int j = 0;
	printf("제품 확인\n");
	for(i = 0;i<prod_count;++i)
	{
		printf("제품명 : %s \t 수량 : ", prod1[i].prodname);
		for(j = 0; j < prod1[i].count; ++j)
		{	
			printf("*");				//수량 만큼 * 표시
		}
		printf("(%d개)\n", prod1[i].count); 		//*이 몇개인지 표시
	}
	sleep(3);
	system("clear");
	screen();
}

//결제 화면
void payment()
{
	printf("구매할 제품 목록 \n");

	int i = 0;
	int choice = 0;           //구매할 제품 번호
	int mulryang = 0;         //구매할 수량
	int adultonly = 0;				//태어난 연도
	int totalprice = 0;				//총 금액

	//제품 목록 출력				
	for(i = 0; i < prod_count; ++i)
	{
		printf("%d.%s - 가격 : %d 원\n재고 : %d개\n성인용품 : %s\n", i+1, prod1[i].prodname, prod1[i].price, prod1[i].count, prod1[i].adult == 1 ? "예" : "아니오"); //adult에서 1이면 예 1이 아니면 아니오
	}
	
	printf("구매할 제품 번호를 선택하세요 : ");
	scanf("%d", &choice);

	if(choice < 1 || choice > prod_count)		//선택한 물품의 번호가 1보다 작거나 재고보다 많으면 잘못된 선택
	{
		printf("잘못된 선택입니다.\n");
	}
	
	// 성인인증
	if(prod1[choice - 1].adult == 1)
	{
		printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
		printf("경고 : 이 제품은 19세 이상만 구매 가능합니다.\n태어난 연도를 입력 하시오. : ");    //주민등록번호 구현이 어려워 태어난 연도로 구별
		scanf("%d", &adultonly);
		printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
		if (adultonly > 2006)						//2006년생 이후로는 구매 불가능
		{
			printf("구매가 불가능 합니다.\n");
			sleep(1);
			system("clear");
			payment();
		}
		else;
		{
			printf("구매가 가능 합니다.\n");
		}
	}
	printf("구매할 수량을 입력하세요 : ");
	scanf("%d", &mulryang);
	if(mulryang > prod1[choice - 1].count)		//입력한 수량이 재고보다 많으면 재고가 부족함.
	{
		printf("재고가 부족합니다. \n");
	}
	//총 금액
	totalprice = prod1[choice-1].price * mulryang;
	printf("총 계산 금액 : %d원 \n", totalprice);

	//구매 방법 선택
	int paychoice = 0;  //구매방법
	int card = 0;       //카드
	int cash = 0;       //현금
	int change = 0;	    //거스름돈

	printf("결제 방법을 선택하시오. (1:카드 2:현금) : ");
	scanf("%d", &paychoice);
	if(paychoice == 1)					//카드 결제
	{
		char card[20];
		printf("카드 입력 : ");
		scanf("%s", card);	//카드 번호
		account += totalprice;				//팔은 가격 만큼 잔고 업데이트
		prod1[choice-1].count -= mulryang;		//팔은 재고 만큼 업데이트
		printf("카드로 결제 했습니다.\n");
	}
	else if(paychoice == 2)
	{
		printf("현금으로 %d원을 지불하세요. : ", totalprice);
		scanf("%d", &cash);
		if(cash < totalprice)
		{
			printf("지불 금액이 부족합니다. \n");
			payment();
		}
		account += totalprice;				//받은 돈 만큼 잔고 업데이트
		prod1[choice-1].count -= mulryang;		//팔린 재고 만큼 업데이트

		change = cash-totalprice;
		printf("거스름돈 : %d 원을 돌려 드립니다.\n", change);
		sleep(1);
		account -= change;				//거스름돈 만큼 잔고에서 빼고 잔고 업데이트
		printf("현금으로 결제 했습니다. \n");
	}
	else
	{
		printf("잘못된 결제 방법입니다. \n");
		payment();
	}

	sleep(2);
	system("clear");
	screen();
}

void fin()
{
	paytime = (int)difftime(end,start) / 60; 		//difftime은 time.h안에 있는 함수로 End-start를 해주는것 int 형으로 받기
	printf("총 일한 시간 : %d 분\n", paytime); 		//전역 변수 paytime
	printf("오늘의 일당 : %d 원\n", paytime*9200);		 //일한 분 만큼 최저 분당 급여인 9200원을 곱함
	printf("잔고 : %d 원\n", account + (paytime*9200));  	//일당 만큼 잔고에 돈이 들어감
	printf("10초후 종료 됩니다.\n");
	sleep(10);
}

void findprod()
{
	int i = 0;
	int found = 0;					//제품 발견 여부
	char find[20];
	printf("찾고자 하는 제품명 : ");
	scanf("%s", find);
	for(i = 0; i < prod_count; ++i)    		//pord_count 는 등록된 제품 수량
	{
		if (!strcmp(find,prod1[i].prodname))
		{
			printf("제품을 찾았습니다.\n제품명 : %s\n가격 : %d \n", prod1[i].prodname, prod1[i].price);
			found = 1;
			break;
		}
	}
	if (!found)
	{
		printf("제품을 발견하지 못했습니다. \n");
	}
	sleep(3);
	system("clear");
	screen();
}
