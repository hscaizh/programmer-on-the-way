'''
题目:
求一个数组中绝对值唯一的数的个数

思路:
用了最简单的方法,连题目中的有序条件都没用到,直接用字典(哈希表)记录绝对值出现的元素,
然后字典中key的个数即为所求


复杂度分析:
O(N)

实现见代码.

https://codility.com/demo/results/demo3BYMX7-7CW/
'''

def solution(A):
    D = {}
    for x in A:
        t = abs(x)
        if t not in D:
            D[t] = 1
    
    print D
    total = 0
    for key in D:
        total += D[key]
    
    return total
