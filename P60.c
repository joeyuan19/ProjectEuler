#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int concat(int x, int y) {
	char * a = "" + x;
	char * b = "" + y;
	printf("%s %s\n",a,b);
	char buf[20];
	/*
	strcat(buf,a);
	strcat(buf,b);
	*/
	return 1;//atoi(buf);
}

int main() {
	int i;
	for (i = 0; i < 10; i++) {
		printf("%d\n",concat(i,i+1));
	}

	return 0;
}
