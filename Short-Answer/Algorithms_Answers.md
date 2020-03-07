#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
while a is less than n cubed, set a to a + n squared. 
This code will run roughly O(2n) times so the runtime complexity is Linear. O(n)


b)
from 0 to n, square the number (j) counting. Return the number of times j has been squared
This code will run roughly O(n^2) times so the runtime complexity is Quadratic O(n^c)

c)
get a number of bunnies, return 2 + numBunnies - 1. 
This code will run roughly O(n4) times, so the runtime complexity is Linear O(n)

## Exercise II
This sounds a lot like quick-sort. So let's try quick-sorting this.

def eggdrop(n_stories):
    middle = n_stores // 2
    broken = True
    first = 0
    last = n_stories - 1
    dropegg from middle:
        if egg doesnt break
        return middle
        
        if broken = true:
            while first <= last and broken:
                middle = (first + last) // 2
                drop egg from middle
                    if broken
                        last = middle - 1
                    if !broken
                        return middle
                
runtime complexity of quick-sort is O(n logn)
