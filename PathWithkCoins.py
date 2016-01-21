'''
Created on Jan 11, 2016

@author: Rahul
'''

def chain(i,j,mat,k):
    if k == 0 and i == 2 and j == 2:
        print "Yo"
        return 1
    if i > 2 or j > 2 or k < 0:
        return 0
    return chain(i+1,j,mat,k-mat[i][j]) + chain(i,j+1,mat,k-mat[i][j])  

if __name__ == '__main__':
    k = 12
    mat = [[1,2,3],[4,5,6],[3,2,1]]
    i = 0
    j = 0
    print chain(i,j,mat,k)