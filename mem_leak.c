#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


int main(int argc , char * argv[])
{
	int lcv = 0;
	for(lcv = 0 ; lcv < 10 ; lcv++)
	{
		char * allocated_string = (char *)malloc(sizeof(char) * 10);
		if ( allocated_string != NULL)
		{
			bzero(allocated_string , sizeof(char) * 10);
			(void)printf("Memery allocated\n");
		}
	}
	return EXIT_SUCCESS;
}
