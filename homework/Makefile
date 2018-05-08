test: main.o p1.o p2.o
	gcc -o test main.o p1.o p2.o
main.o: main.c h1.h h2.h
	gcc -c main.c
p1.o: p1.c h1.h h2.h
	gcc -c p1.c
p2.o: p2.c h1.h h2.h
	gcc -c p2.c

.PHONY: clean
clean:
	rm -f *.o
