#author:hscaizh
#create on Nov 4, 2014

'''
题目:
求M次,[p,q]区间内的满足条件为两个素数乘积的数的个数,p<=q<=N,时间复杂度要求为
O(N*log(log(N))+M);

思路:
简单,用sieve-of-eratosthenes算法得到每个数的最小的因子,对每个数判断除去因子后的另一个数是否是素数,用F1记录到每个数时之前的数满足条件的数的个数.

实现见代码.
'''

def solution(N, P, Q):
    F, F1= [0]*(N+1), [0]*(N+1)
    M = len(P)
    
    i = 2
    while i*i <= N:
        if F[i] == 0:
            k = i*i
            while k <= N:
                F[k] = i
                k += i
        i += 1
    
    for i in xrange(4,N+1):
        if F[i] != 0 and F[i/F[i]] ==0:
            F1[i] = F1[i-1] + 1
        else:
            F1[i] = F1[i-1]
    
    retv = []
    
    for i in xrange(M):
        retv.append(F1[Q[i]]-F1[P[i]-1])
    
    return retv
