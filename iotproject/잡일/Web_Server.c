#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define BUF_SIZE 1024
char* get_content_type(const char* path);

int main(int argc,int argv[])
{
	int serv_sock, clnt_sock;
	char buf[BUF_SIZE];
	struct sockaddr_in serv_adr, clnt_adr;
	socklen_t clnt_adr_sz;
	
	FILE* fp;
	char html[BUF_SIZE];
	size_t read_bytes;

	fp = fopen("index.html","r");
	if(fp == NULL)
	{
		perror("index.html 파일을 열 수 없습니다.");
		exit(1);
	}

	serv_sock = socket(PF_INET, SOCK_STREAM, 0);
	if (serv_sock == -1)
	{
		perror("socket() error");
		exit(1);
	}

	memset(&serv_adr, 0, sizeof(serv_adr));
	serv_adr.sin_family = AF_INET;
	serv_adr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_adr.sin_port = htons(atoi(argv[0]));

 	if(bind(serv_sock, (struct sockaddr*)&serv_adr, sizeof(serv_adr)) == -1)
	{
		perror("bind() error");
		exit(1);
	}
	
	if(listen(serv_sock, 5) == -1)
	{
		perror("listen() error");
		exit(1);
	}

	printf("웹서버 실행중... <port> : %d\n", argv[0]);

	while(1)
	{
		clnt_adr_sz = sizeof(clnt_adr);
		clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_adr, &clnt_adr_sz);

		read(clnt_sock, buf, BUF_SIZE -1);
		printf("요청 : \n%s\n", buf);

		char method[10], path[100];
		sscanf(buf, "%s %s", method, path);

		if(strcmp(method, "GET") != 0)
		{
			close(clnt_sock);
			continue;
		}

		char file_path[100];
		if(strcmp(path, "/") == 0)
			strcpy(file_path, "index.html");
		else
			strcpy(file_path, path + 1);

		FILE* fp = fopen(file_path, "rb");
		if(!fp)
		{
			char not_found[] =
				"HTTP/1.1 404 Not Found\r\n"
				"Content-Type: text/html\r\n\r\n"
				"<h1>404 Not Found</h1>";
			write(clnt_sock, not_found, strlen(not_found));
			close(clnt_sock);
			continue;
		}

		char* content_type = get_content_type(file_path);
		char header[BUF_SIZE];
		sprintf(header,
				"HTTP/1.1 200 OK\r\n"
				"Content-Type : %s\r\n\r\n", content_type);
		write(clnt_sock, header, strlen(header));

		size_t n;
		while ((n = fread(buf, 1,BUF_SIZE, fp)) > 0)
		{
			write(clnt_sock, buf, n);
		}
	}

	fclose(fp);
	close(serv_sock);

	return 0;
}

char* get_content_type(const char* path)
{
	if (strstr(path, ".html")) return "text/html";
	if (strstr(path, ".png")) return "image/png";
	if (strstr(path, ".jpg") || strstr(path, ".jpeg")) return "image/jpeg";
	return "text/plain";
}
