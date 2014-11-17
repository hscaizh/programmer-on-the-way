'''
题目:
这道题前面的课程似乎出现过
求一个数组中任意3个元素满足三角形两边之和大于第三边的个数,注意这里不需要考虑边长>0
时间复杂度要求 O(N^2)

思路:
排序之后从前往后扫,具体见代码


复杂度分析:
排序 O(N*log(N))
平摊分析 O(N^2)
共O(N^2))

实现见代码.

解题地址: https://codility.com/demo/results/demoF32ZZ7-8TX/
'''

def solution(A):
    A.sort()
    n = len(A)
    result = 0
    
    for x in xrange(n):
        z = x
        for y in xrange(x+1,n):
            while z < n and A[x]+A[y] >A[z]:
                z += 1
            result += z - y - 1
    
    return result
