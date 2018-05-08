#include <stdio.h>
#include "h1.h"
#include "h2.h"

void p1func() {
	printf("I am p1func!\n");
}

void p1func2() {
	p2func();
}
