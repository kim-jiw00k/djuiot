#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>    // 파일 불러오기 모듈 참조
#include <unistd.h>  // close 사용 하는 모듈 참조

void main()
{
	int fd;
	fd = open("a.txt", O_CREAT | O_RDONLY);
	if(fd < 0)
	{
		perror("Could not open a.txt");
		exit(1);
	}else
	{
		printf("open success");
		printf("file descriptor : %d\n", fd);
	}
	close(fd);
}
