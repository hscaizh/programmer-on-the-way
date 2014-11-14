'''
题目:
A,B数组,A[i],B[i]表示木板i的区间,C数组,C[k]表示钉子k的钉的位置.
求问至少要C的前面多少个,才能保证所有的木板都被至少一颗钉子钉住.
A,B长度为N, C长度为M, 数组元素取值[0,2M]
复杂度要求:时间:O((N+M)*log(M)), 空间:O(M)

思路:
钉子的个数可以半分查找,于是问题变成如何在log(N+M)的时间内判断是否全部木板被钉住.
由于元素取值[0,2M],用D[i]记录0~i区间总共的钉子数,于是D[B[i]]-D[A[i]-1]>0即可判定木板i
被钉住.

复杂度分析:

空间复杂度 O(2M)
时间复杂度 O(2M+M+2M+N)=O(5M+N) < O(5M+5N)=O(M+N)
于是总时间复杂度符合要求

实现见代码.

可能有更好解法

解题地址:  https://codility.com/demo/results/demoM9DKB6-N6H/
'''

def solution(A, B, C):
    M = len(C)
    N = len(A)
    
    D = [0]*(2*M + 1)
    
    def check(k):
        for i in xrange(2*M+1):
            D[i] = 0
            
        for i in xrange(k):
            D[C[i]] = 1
            
        for i in xrange(1,2*M+1):
            D[i] += D[i-1]
        
        
        for i in xrange(N):
            if D[B[i]] - D[A[i]-1] <= 0:
                return False
        
        return True
    
    begin = 0
    end = M
    
    result = -1
    while begin <= end:
        mid = (begin+end)/2
        if (check(mid)):
            end = mid -1
            result = mid
        else:
            begin = mid +1
    
    return result
            
