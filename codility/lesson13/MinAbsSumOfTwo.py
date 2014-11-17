'''
题目:
求一个数组中任意两个元素之和绝对值最小是多少?
时间复杂度要求 O(N*log(N))

思路:
简单,先排序,蠕虫方法,然后两头扫


复杂度分析:
排序 O(N*log(N))
平摊分析 O(N)
共O(N*log(N))

实现见代码.

解题地址: https://codility.com/demo/results/demoPTG64V-3SN/
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
