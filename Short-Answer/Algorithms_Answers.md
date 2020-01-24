#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This runtime is constant - O(1).  This runtime will not change whatever the input for n is.  It will only use that input to perform a calculation.


b) This runtime logarthimic - O(logn).  As n increases, the runtime, or number of operations performed will grow at a slower rate.  This is because 'j' will be doubled everytime an iteration is performed, whereas 'n' grows at a constant rate.  Therefore, the number of iterations required for 'j' to hit 'n' will grow at a slower rate because 'j' will be growing much faster than 'n', and the operations will stop as soon as 'j' becomes greater than 'n'. 


c)  This runtime is linear - O(n).  As the size of n increases, the number of operations performed (as well as the amount of space used) will grow at the same rate.  In this case, it calls the function 'bunnies' at a linear rate.  However, it should be noted that since this function is recursive, it will use more space than an iterative function.

## Exercise II

**As part of this answer, I will assume the buildings floor are already in order from lowest to highest**

In order to solve this solution and minimize the number of eggs dropped, I would follow the example of binary search in order to find the correct floor 'f.'  To do this I would find the middle floor, this I would do by dividing the top floor by 2.  I would go to that floor and drop an egg.  

If the egg broke, I would know that either I was on floor 'f' or that it was below me.  From there, I would find the middle floor between the current floor I was on and the bottom floor (divide the current floor I was on by 2) to continue my experiment

If the egg didn't break, I would know that floor 'f' must be somewhere above me.  I would then calculate the middle floor between where I was and the top floor.  I would go to that floor to continue the experiment.  

In short, if the egg broke, I would move down by half the floors remaining.  If it didn't break, I would move up by half the floors remaining.  I would repeat the process until I was able to find floor 'f.' 

The run time for this operation would be logarthmic - O(log n).  Because every operation would eliminate half the floors remaining until 'f' was found.  This would be much more effecient than a linear search (ex starting on the first floor and working your way up) because each operation would only eliminate one possibilty until 'f' was found.  However, in this case it would minimize the number of eggs broken.  
