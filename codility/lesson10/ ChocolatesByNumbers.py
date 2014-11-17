#author:hscaizh
#create on Nov 4, 2014

'''
题目:


思路:

这道题想了很久,关键是没有看清题目条件的数的取值范围,一眼看去以为是2^N

取值范围为[1,2*N]就很明朗了,先排序(避免重复数字多次计算,然后遍历排序后的数组B中记录[1,2N]之间是B[i]的倍数.

复杂度分析:

排序O(N*logN),记录个数 < O(sieve-of-eratosthenes(2N)) ~= O(NloglogN) < O(NlogN)
故最终复杂度为O(NlogN),符合题目要求

实现见代码.
'''

def solution(A):
    N = len(A)
    F = [0]*(2*N+1)
    B = [x for x in A]
    B.sort()
    
    i = 0
    while i < N:
        weight = 1
        while i+1 < N and B[i+1] == B[i]:
            weight += 1
            i += 1
        
        k = B[i]
        while k <=2*N:
            F[k] += weight
            k += B[i]
        
        i += 1
    
    retv = []
    for x in A:
        retv.append(N-F[x])
    
    return retv


