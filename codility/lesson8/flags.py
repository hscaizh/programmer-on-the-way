#author:hscaizh
#create on Nov 4, 2014

'''
题目:
一个数组中,"山峰"是指比其两边元素都大的元素(故首尾元素不可能是山峰).
一个人携带K面旗游览数组,可以在山峰插旗,两面旗之间的距离必须大于K.
求k的最大值.

思路:
N为数组元素个数
记录山峰间的间距
当K=t时,(t-1)*t<=N-2,需要的操作最多为t次
1+2+..+n^(1/2) = O(n)

实现:
取t的值为(0,int(n^0.5)+1),从大到小,第一个可行的t即为所求

优化:
查找K时,可以用二分而不是遍历(不能赞更多)

'''

def solution(A):
    N = len(A)
    B = []
    if N <3:
        return 0
    
    last_peak = None
    
    for i in xrange(1,N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            new_peak = i
            if last_peak != None:
                B.append(new_peak-last_peak)
            else:
                B.append(0)
            last_peak = new_peak
    
    npeaks = len(B)
    
    if len(B) == 0 or len(B) == 1:
        return len(B)

    def check(i):
        dis = i
        nflags = 0
        n = npeaks
        for x in B:
            n -= 1
            dis += x
            if dis >= i:
                nflags += 1
                dis = 0
            if nflags >=i:
                return True 
            if n+nflags < i:
                return False

        return True
    
    retu = 1
    for i in xrange(int(N**0.5)+1,1,-1):
        if check(i):
            retu = i
            break
    
    return retu
