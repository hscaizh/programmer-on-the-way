'''
题目:
DistinceSlices定义:没有重复元素的子数组
求一个数组中没有重复元素的子数组的个数
条件:数组中每个元素的取值范围[0,M]
时间复杂度要求 O(N)
空间复杂度要求 O(M)

思路:
简单,蠕虫方法,从前往后扫


复杂度分析:
平摊分析 O(N)

实现见代码.

解题地址:  https://codility.com/demo/results/demoC8URBJ-JWV/
'''

def solution(M, A):
    N = len(A)
    y = 0
    D = [0]*(M+1)
    result = 0
    
    for x in xrange(N):
        while y < N and D[A[y]] == 0:
            D[A[y]] += 1
            y += 1
        
        #print x,y,D
        result += y-x
        
        D[A[x]] -= 1
    
    result = 1000000000 if result > 1000000000 else result
        
    
    return result
