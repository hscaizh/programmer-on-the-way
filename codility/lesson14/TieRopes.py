'''
题目:
n根绳子排成一行,每根长度为A[i],相邻绳子可以系在一起长度为之和,现在需要长度>=K的绳子,
问最多能产生多少根?

思路:
贪心的题关键是证明,定义f(i)为从i开始最多有多少,则有f(k)>=f(k+1),
f(k+1)+1>=f(k)
从而直接从左往右系,绳子长度满足了就开始新的一根

复杂度分析:
O(N)

实现见代码.

https://codility.com/demo/results/demoBZR38E-XPF/
'''

def solution(K, A):
    result = 0
    
    rl = 0
    for x in A:
        rl += x
        if rl >= K:
            rl = 0
            result += 1
    
    return result
