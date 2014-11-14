'''
题目:
求一个数组在分成k个子数组时,子数组的和中最大值最小是多少.
条件:数组中每个数取值范围[0,M],共有N个元素,子数组可以为空
复杂度要求: 时间:O(N*log(N+M)) 空间:O(1)


思路:
设"子数组的和中最大值最小值"为t,则t的范围为[max(A),sum(A)],
然后在这个范围空间二分查找t,每一次查找耗时为O(N)

复杂度分析:
O(N)*O(sum(A)-max(A)),应该是O(N*log(N*M)),可能有更好的解法

实现见代码.

解题地址:  https://codility.com/demo/results/demoERY7ED-2N8/
'''

def check(A, k):
    N = len(A)
    blocks = 0
    last = -1
    
    s = 0
    
    for i in xrange(N):
        s += A[i]
        if (i+1) < N and (s+A[i+1]) > k:
            blocks += 1
            s = 0
    blocks += 1
    return blocks
        


def solution(K, M, A):
    N = len(A)
    end = sum(A)
    begin = max(A)
    result = -1
    
    while begin <= end:
        mid = (begin+end)//2
        if check(A,mid) <= K:
            end = mid - 1
            result = mid
        else:
            begin = mid + 1
    
    return result
            
