#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"SHELLCODE ";    /* paste the hex bytes in between those quotes */

main()
{

	printf("Shellcode Length: %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();


}


/* gcc -fno-stack-protector -z execstack shellcode.c -o shellcode */
