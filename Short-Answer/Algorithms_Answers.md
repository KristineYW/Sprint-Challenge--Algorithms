#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime complexity: linear O(n)
    Although the conditional for the while loop checks a against n^3, a itself increments by n*n (plus a) inside of the loop, so the runtime complexity of the entire while loop is closest to being linear.


b) Runtime complexity: linearithmic O(n * log_2 n)
    This is a nested loop situation where the outer range includes 0-n and runs j = 1 "n" number of times, making the outer loop's big O value O(n). Since the nested while loop dictates that the value of j multiples on each loop, it is similar to a logarithmic function with log base 2, as the value of j always doubles and the inner while loop will run for a significantly shorter amount of iterations than n, making the inner big O notation O(log_2 n). The final big O notation is the mulplicative value of the inner and outer loops.  


c) Runtime complexity: linear O(n)
    This is a simple recursion using a base case of bunnies == 0 and decrements bunnies until it reaches the base case. Since the runtime increases and decreases linearly based on the size of the input bunnies, the function has a O(n) runtime. 

## Exercise II

Understanding the problem:

It sounds like we are searching for the specific floor in a building with a number of floors, for which if an egg was thrown off that floor and all floors above it, the egg would break. If the egg was thrown off any floor below it, the egg does not break. 

We are calling the specific floor we are looking for "f" and the number of total floors in the building is "n".

We are trying to find the ideal way of searching for f, likely so as to minimize the number of eggs we have to waste in throwing off the building on our quest to find f. 

Planning a solution:

It sounds like we need a searching algorithm. The two we know of are linear and binary. The only way that binary search is less "efficient" than linear (where we would throw an egg off every floor from the ground up) would be if the floor number happens to be under the maximum depth size for the binary search. Going into the problem blind, however, binary solutions are always preferred. Thus, we will go with the binary approach.

We are searching for a numerical value of "f" given a range of (0,n). We can also start with an assumption on the boolean value for whether the egg breaks.

Binary search dictates that we should start in the midpoint of the sorted range, or 1/2n, and determine whether the egg is broken at that point. If it is, we can cut the list in half and only search in the list below 1/2 since we know f is now in the range of (0, 1/2n). If the egg remains intact, then we know that f lies somewhere between (1/2n, n). We repeat this methodology, comparing the boolean values using a new midpoint, recursively until we can pinpoint exactly where the egg does not break on floor "f-1" to where it breaks on floor "f". 

This binary search method has a runtime complexity of O(log_2 n)