This is a quick program to show the impact of different implementations of calculating fibonacci numbers.

Ways it's calculated:
Naive recursive: fib(n) = fib(n-1) + fib(n-2). This is O(2^N), it will quickly take too long to get values if you use this.
Better recursive: above, but with memoization. O(N) but O(N) space
Iterative: calculate the values and track only current, and previous two values. O(N) time and O(1) space.

In the main file you can set the N to calculate and if you want Iterative, Recursive (naive), and/or recursive (with memo). 

Comparing iterative and recursive with memoization is pretty interesting since they have the same bigO runtime, but the slopes are quite different.
