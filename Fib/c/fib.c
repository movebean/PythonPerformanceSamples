#include <stdio.h>
#include <sys/time.h>
long fib(int num)
{
				if (num <= 1)
								return 1;
				else
								return fib(num - 1) + fib(num -2);
}

long getCurrentTime()
{
				struct timeval tv;
				gettimeofday(&tv, NULL);
				return tv.tv_sec * 1000 + tv.tv_usec / 1000;
}

int main(void)
{
				long start, end;
				start = getCurrentTime();
				printf("%ld\n", fib(45));
				end = getCurrentTime();
				printf("time %ld\n", end - start);
				return 0;
}
