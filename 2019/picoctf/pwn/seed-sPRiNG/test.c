/* srand example */
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <unistd.h>    /* sleep */

int main ()
{
  srand(time(0));
  for(int i=0;i<30;i++){
    printf("%d\n", rand()&0xf);
  }
  return 0;
}
