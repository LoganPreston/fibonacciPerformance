import time
import matplotlib.pyplot as plt


def fib(n):
    if n < 2:
        return n

    memo = [0] * (n + 1)
    memo[1] = 1
    return fibRecurse(n, memo)


def fibRecurse(n, memo):
    if n == 0:
        return 0

    if memo[n] > 0:
        return memo[n]

    memo[n] = fibRecurse(n - 1, memo) + fibRecurse(n - 2, memo)
    return memo[n]


def fibNaive(n):
    if n < 2:
        return n

    return fibNaive(n - 1) + fibNaive(n - 2)


def fibIter(n):
    if n < 2:
        return n

    a = 0
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c

    return a + b


def test(num, iterative, recursive, recursiveWithMemo):
    results = [0]*num
    
    for i in range(0,num):
        start = time.time()
        if(iterative):
            fibIter(i)
        end = time.time()
        fibIterTime = end - start

        start = time.time()
        if(recursiveWithMemo):
            fib(i)
        end = time.time()
        fibRecurseTime = end - start

        start = time.time()
        if(recursive):
            fibNaive(i)
        end = time.time()
        fibRecurseNaiveTime = end - start

        results[i] = [i, fibIterTime, fibRecurseTime, fibRecurseNaiveTime]

    return results


def main(n, iterative, recursive, recursiveWithMemo):
    results = test(n, iterative, recursive, recursiveWithMemo)
    nums = [val[0] for val in results]

    #plot setup
    fig, ax = plt.subplots(figsize=(10, 6), num="Performance")

    #plot the raw data
   
    if iterative:
        fibIter = [val[1] for val in results]
        ax.scatter(nums, fibIter, c="orange", marker="D", label="Iterative")
   
    if recursiveWithMemo:
        fibRecurseMemo = [val[2] for val in results]
        ax.scatter(nums, fibRecurseMemo, c="blue", label="Recursive with memoization")
   
    if recursive:
        fibRecurse = [val[3] for val in results]
        ax.scatter(nums, fibRecurse, c="green", marker="x", label="Recursive")

    #display and hold until user interacts
    plt.xticks(nums[1::2])
    ax.set_xlabel('Fibonacci input')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Performance of Calculating Fibonacci value')
    #ax.set_yscale('log', basey=2)
    #ax.set_xscale('log', basex=2)
    ax.legend()
    plt.show()
    print()

main(20, True, True, True)
