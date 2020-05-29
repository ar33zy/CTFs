#include <stdio.h> 
#include <stdlib.h> 
  
int main(void) 
{ 
    srand(1585599106);
    for(int i = 0; i<374109; i++)
        printf("%d\n", rand()); 
    return 0; 
} 
