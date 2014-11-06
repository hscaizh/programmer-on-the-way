#author:hscaizh
#create on Nov 4, 2014

'''
题目:
N个巧克力摆成一圈,从0开始,每隔M个(糖纸)吃一个,吃完了留下糖纸,问最后能吃多少个巧克力.

思路:

实际上是数学题,出在这课里明显就是提示跟公约数有关系.
分析能够吃到哪些巧克力{Mx+Ny}modN,例子中就是(4x+10y)mod10
公约数的一条定理:a,b公约数为{ax+by}集合中的最小元素
{4x+10y}mod10显然又都是公约数的倍数.

于是求出公约数d,用N除去d即为能吃到的巧克力个数

复杂度分析:

求公约数复杂度 O(log(N+M))

实现见代码.

解题地址:https://codility.com/demo/results/demoKUCRCT-42K/
'''

def solution(N, M):
    def gcd(a,b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    
    return N//gcd(N,M)


