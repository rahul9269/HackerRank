'''
Created on Jan 11, 2016

@author: Rahul
'''
dp  = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
def  count(i,j,m,n,k,dir):
    if i == m - 1 and j == n - 1:
        return k == 0
       
    if i > m - 1 or j > n - 1:
        return 0
    if not dp[i][j] == -1:
        return  dp[i][j] 
    if dir == "down":
        i +=1
        dp[i][j]= count(i,j,m,n,k,"down") + count(i,j,m,n,k-1,"right")
    else:
        j +=1 
        dp[i][j]= count(i,j,m,n,k-1,"down") + count(i,j,m,n,k,"right")
    return dp[i][j]

if __name__ == '__main__':
    k = 2
    m = 3
    n = 3
    i = 0
    j = 0
    dp [0][0] = 0
    print count(i,j,m,n,k,"down") + count(i,j,m,n,k,"right")