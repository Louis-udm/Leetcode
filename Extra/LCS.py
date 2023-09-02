'''
Optimized LCS dynamic programming algorithm
Examples: 
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3. 
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4. 

https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

'''

import numpy as np


'''
LCS dynamic programming algorithm
Time Complexity: O(n*m)
Auxiliary Space: O(n*m)
'''
def LCS_DP_str(strA,strB):
    n=len(strA)
    m=len(strB)
    # dp table是(n+1) x (m+1), 
    # index: dp table 1,2,3 对应 str 0,1,3
    # 原因是dp[i-1]的时候不会出界，
    # 并且i=1时, 表示计算(s1[0],s2[0]), dp[0]和dp[:0]=0,因为str[0]前面没有字母
    dp_table=np.zeros((n+1,m+1),dtype=int)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if strA[i-1] == strB[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i - 1][j])
    print(dp_table)
    return dp_table[n][m]

def LCS_DP_array(arrayA,arrayB):
    """Optimized LCS dynamic programming algorithm

    parameters
    ----------
    arrayA : numpy array
        first array
    arrayB : numpy array
        second array
    
    returns
    -------
    lcs length

    """
    n=len(arrayA)
    m=len(arrayB)
    dp_table=np.zeros((n+1,m+1),dtype=int)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arrayA[i-1] == arrayB[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i - 1][j])
    return dp_table[n][m]

'''
Recursive approach
'''
def lcs_recursive(X, Y, m, n):
    # https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
    # Time Complexity: O(2n)
    # Auxiliary Space: O(n)
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs_recursive(X, Y, m-1, n-1);
    else:
       return max(lcs_recursive(X, Y, m, n-1), lcs_recursive(X, Y, m-1, n));
 
 
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
# print ("Length of LCS is ", lcs_recursive(X, Y, len(X), len(Y)))
print ("Length of LCS is ", LCS_DP_str(X, Y))


def s1():
    lcs_recursive(X, Y, len(X), len(Y))


def s2():
    LCS_DP_str(X,Y)


import timeit

# print(timeit.timeit(s1, number=10000))
# print(timeit.timeit(s2, number=10000))
