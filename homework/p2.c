#include <stdio.h>
#include "h1.h"
#include "h2.h"

void p2func() {
	printf("I am p2func!\n");
}

void p2func2() {
	p1func();
}
